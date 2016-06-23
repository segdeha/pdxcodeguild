requirejs(
    [
        './jquery',
        './semantic',
        './ingredients-updater',
        './total-updater',
        './validator',
        './thanks'
    ],
    function ($, semantic, updateIngredients, totalUpdater, validate, thanks) {

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

        form.addEventListener('change', function (evt) {
            totalUpdater.updateTotal(form, total_output, costs);
            updateIngredients(form, ingredients_output, ingredients);
            // that updates class based on credit

            // update credit card icon on page
            var ccType = validator.ccType();
            var span = form.querySelector('#cc-type');
            span.className = undefined; // clear current class
            span.className = ccType; // update current class
        });

        form.addEventListener('submit', function (evt) {
            if (!validate(form, requiredFields)) {
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
