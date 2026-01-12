# Commit Message Conventions

This project follows the [Conventional Commits](https://www.conventionalcommits.org/) specification. This leads to more readable messages that are easy to follow when looking through the project history.

## Format

```text
<type>(<scope>): <description>

[optional body]

[optional footer(s)]
```

### Type
Must be one of the following:

- **feat**: A new feature
- **fix**: A bug fix
- **docs**: Documentation only changes
- **style**: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
- **refactor**: A code change that neither fixes a bug nor adds a feature
- **perf**: A code change that improves performance
- **test**: Adding missing tests or correcting existing tests
- **build**: Changes that affect the build system or external dependencies (example scopes: pip, npm)
- **ci**: Changes to our CI configuration files and scripts
- **chore**: Other changes that don't modify src or test files
- **revert**: Reverts a previous commit

### Scope (Optional)
The scope should be the name of the Django app or component affected (e.g., `Items`, `Users`, `settings`).

### Description
The description contains a succinct description of the change:
- Use the imperative, present tense: "change" not "changed" nor "changes"
- Don't capitalize the first letter
- No dot (.) at the end

## Examples

- `feat(Items): add stock balance calculation to viewset`
- `fix(Users): resolve JWT token expiration issue`
- `docs(README): updated setup instructions`
- `build(pip): add drf-spectacular for api documentation`
- `refactor(Items): clean up serializer validation logic`
