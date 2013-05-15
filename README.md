# django-memento

## Installation
    pip install django-memento

## Usage

```python
from memento.helpers import Logger
Logger.log(message, object, severity):
```

* **message:** a string
* **object:** can be a model
* **severity** is a number from 1-5
 * 1: Very low
 * 2: Low
 * 3: Medium
 * 4: High
 * 5: Very High

## Settings

### MEMENTO_SEVERITY_CHOICES
Can be used to define your own severity choices.
