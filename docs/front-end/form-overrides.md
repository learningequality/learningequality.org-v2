# Form overrides

## Changing the markup depending on `widget_type`

`field.html` outputs all of the markup for all of the form fields.

If you need to add additional markup to a specific form field you can do so by checking the widget type.

Here's how you would wrap a date field input in a `div`:

```html
{% if widget_type == 'date-input' %}
<div>
  <label for="{{ field.id_for_label }}" class="field__label">
    {{ field.label }} {% if field.field.required %}<span
      class="field__required"
      aria-hidden="true"
      >*</span
    >{% endif %}
  </label>
  {{ field }}
</div>
{% endif %}
```

`widget_type` corresponds to [Django’s widget class names](https://docs.djangoproject.com/en/3.0/ref/forms/widgets/), written in kebab-case instead of TitleCase. For example `CheckboxInput` -> `checkbox-input`.

## Adding field attributes

Have a look at `project_styleguide/forms.py` for examples.
