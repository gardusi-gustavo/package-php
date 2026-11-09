# package-php

PHP reference package: a Composer library, a web example, PHPUnit tests, and
Packagist release notes.

## Layout

| Path | Holds |
| --- | --- |
| `src/` | publishable library |
| `tests/` | PHPUnit tests |
| `examples/web-app/` | full web example |
| `docs/` | usage and release notes |

## Build

```bash
composer install
vendor/bin/phpunit
```
