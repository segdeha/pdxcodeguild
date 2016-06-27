requirejs(
    [
        './jquery',
        './semantic',
        './ingredients-updater',
        './total-updater',
        './validator',
        './thanks'
    ],
    function ($, semantic, updateIngredients, totalUpdater, validator, thanks) {

    // initialize semantic-ui checkboxes and radio buttons
    $('.ui.checkbox').checkbox()

    var total_output, ingredients_output, thanks_output, ingredients, requiredFields;
    var costs = { 'extra-ingredients': 0.5, 'delivery': 5 };
    var form = document.querySelector('form');

    if (form) {
        total_output = document.getElementById('total_cost');
        ingredients_output = document.getElementById('ingredients');
        costs = { 'extra-ingredients': 0.5, 'delivery': 5 }; // TODO expose this from a module to make things ore DRY
        ingredients = ['tortilla', 'meat', 'included-ingredients', 'extra-ingredients'];
        requiredFields = ['name', 'credit-card', 'cvv', 'zip', 'terms'];

        form.addEventListener('keyup', function (evt) {
            // update credit card icon on page
            var field = form.querySelector('#credit-card');
            var ccType = validator.creditCardType(field.value);
            var span = form.querySelector('#cc-type');
            span.className = ccType;
        });

        form.addEventListener('change', function (evt) {
            totalUpdater.updateTotal(form, total_output, costs);
            updateIngredients(form, ingredients_output, ingredients);
        });

        form.addEventListener('submit', function (evt) {
            if (!validator.validate(form, requiredFields)) {
                // prevent the form from submitting when the user hits the submit button
                evt.preventDefault();
            }
        });
    }
    else {
        thanks_output = document.getElementById('order-details');
        thanks(thanks_output, costs);
    }
});
