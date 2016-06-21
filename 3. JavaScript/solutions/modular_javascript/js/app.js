requirejs(
    [
        './jquery',
        './semantic',
        './ingredients-updater',
        './total-updater',
        './validator'
    ],
    function ($, semantic, updateIngredients, updateTotal, validate) {

    // initialize semantic-ui checkboxes and radio buttons
    $('.ui.checkbox').checkbox()

    var form = document.querySelector('form');
    var total_output = document.getElementById('total_cost');
    var ingredients_output = document.getElementById('ingredients');
    var costs = { 'extra-ingredients': 0.5, 'delivery': 5 };
    var ingredients = ['tortilla', 'meat', 'included-ingredients', 'extra-ingredients'];
    var requiredFields = ['name', 'credit-card', 'ccv', 'zip', 'terms'];

    form.addEventListener('change', function (evt) {
        updateTotal(form, total_output, costs);
        updateIngredients(form, ingredients_output, ingredients);
    });

    form.addEventListener('submit', function (evt) {
        // prevent the form from submitting when the user hits the submit button
        evt.preventDefault();
        validate(form, requiredFields);
    });
});
