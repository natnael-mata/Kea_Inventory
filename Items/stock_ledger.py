from django.db.models import Sum
from .models import Items, Items_InitialAmount, Transactions, Items_Price
from django.utils import timezone

def get_stock_ledger(item_id=None, start_date=None, end_date=None):


    if not end_date:
        end_date = timezone.now()
        
    ledgers = []
    
    # Filter items
    items_qs = Items.objects.all()
    if item_id:
        items_qs = items_qs.filter(item_id=item_id)
        
    for item in items_qs:
        ledger_entries = []
        running_balance = 0

        start_initial_qty = 0
 
        
        base_date = start_date if start_date else end_date
        
        initial_record = Items_InitialAmount.objects.filter(
            item_id=item.item_id,
            effective_date__lte=base_date
        ).order_by('-effective_date').first()

        effective_start_date = None
        
        if initial_record:
            running_balance = initial_record.quantity
            effective_start_date = initial_record.effective_date
            
            # Add Initial Balance as the first line item
            ledger_entries.append({
                'item_code': item.item_id,
                'item_name': item.item_name,
                'date': initial_record.effective_date,
                'price': _get_price(item.item_id, initial_record.effective_date), # Helper
                'trans_type': 'Initial Balance',
                'quantity': initial_record.quantity,
                'balance': running_balance
            })
        else:
            # No initial record found before date
            pass
        
        trans_qs = Transactions.objects.filter(item_id=item.item_id).order_by('trans_date')
        
        if effective_start_date:
            trans_qs = trans_qs.filter(trans_date__gte=effective_start_date) 
        if start_date:
             trans_qs = trans_qs.filter(trans_date__gte=start_date)
        if end_date:
             trans_qs = trans_qs.filter(trans_date__lte=end_date)
             
        for trans in trans_qs:

            qty = trans.quantity 
            
            running_balance += qty
            
            ledger_entries.append({
                'item_code': item.item_id,
                'item_name': item.item_name,
                'date': trans.trans_date,
                'price': _get_price(item.item_id, trans.trans_date),
                'trans_type': trans.trans_type,
                'quantity': qty,
                'balance': running_balance
            })
            
        ledgers.extend(ledger_entries)
        
    return ledgers

def _get_price(item_id, query_date):
    price_obj = Items_Price.objects.filter(
        item_id=item_id,
        effective_date__lte=query_date
    ).order_by('-effective_date').first()
    return price_obj.unit_price if price_obj else 0
