/**
 * Validate a form, display error messages if validation fails.
 * @desc The HTML is structured in such a way that all <label></label> tags are
 * siblings of their corresponding <input> tags. Show the error state for a
 * field by adding the class name of `error` to the <label></label>. Clear the
 * error state by removing the class name of `error`. Also, show a summary of
 * the errors near the top of the page between "Customize Your Burrito" and
 * "Your Burrito’s Details" in the following format:
 * <div class="ui error message">
 *     <i class="close icon"></i>
 *     <div class="header">Please correct the following errors before
 *         proceeding.</div>
 *     <ul id="errors" class="list">
 *         <li>Enter your name.</li>
 *         <li>Enter a credit card number.</li>
 *         <li>Enter your credit card’s verification number
 *             (<a href="https://www.cvvnumber.com/">CVV</a>).</li>
 *         <li>Enter the ZIP Code associated with the credit card.</li>
 *         <li>Agree to the Terms &amp; conditions.</li>
 *     </ul>
 * </div>
 * @param {DOM element} form Reference to the DOM element for the <form></form>
 *
 * @param {Array.<string>} requiredFields Array of the names of the fields that
 *     are required to have values
 * @return {Boolean} Returns `true` if the form validation passed, `false` if it
 *     didn’t
 */


define(function () {

    function isValidName(value) {
      if (/^[a-zA-Z\s]*$/.test(value))
        return true
      else {
        return false
      }
    }

    function isValidCC(value) {
      if (string.length === 15) {
        if (type === 'amex') {
          if ((/^(\d{15}\-?|\s)$/).test(value))
            return true
        }
      }
      else if (string.length === 16) {
        if (type === 'visa' || type === 'mastercard' || type === 'discover'){
          if ((/^(\d{16}\-?|\s?)$/).test(value))
            return true
        }
      }
      else {
          return false
      }
    }

    function isValidCVV(type, value) {
      if (type === 'amex') {
        if (/^\d{4}$/.test(value))
          return true
      }
      else if (type === 'visa' || type === 'mastercard' || type === 'discover') {
        if (/^(\d{3})$/.test(value))
        return true
      }
      else {
        return false
      }
    }

    function isValidZip(value) {
      if (/^(\d{5})$/.test(value))
        return true
      else {
        return false
      }
    }

    function isChecked(value) {
      if (value !== "")
        return true
      else {
        return false
      }
    }

    // Get credit card type based on field type string
    function creditCardType(field){
      var firstNumber = field.charAt(0);
      //capitalize first
      switch(firstNumber){
        case '3':
          return 'amex';
          break;
        case '4':
          return 'visa';
          break;
        case '5':
          return 'mastercard';
          break;
        case '6':
          return 'discover';
          break;
        default:
          return ''

      }}


    function validate(form, requiredFields) {
      requiredFields.forEach(function(field) {
        var ccType = creditCardType(form[field].value);
        switch(field) {
          case 'name':
            if (!isValidName(form[field].value)) {
              lis.push(`<li>Enter your name.</li>`);
              break;
            }
          case 'credit-card':
            // store credit card type for cvv
            if (ccType = ""){
              lis.push(`<li>Enter a credit card number.</li>`);
              break;
            }
            else if (!isValidCC(ccType, form[field].value)) {
              lis.push(`<li>Enter a credit card number.</li>`);
              break;
            }
          case 'ccv':
            if (!isValidCVV(ccType, form[field].value)) {
              lis.push(`<li>Enter your credit card’s verification number
 *             (<a href="https://www.cvvnumber.com/">CVV</a>).</li>`);
              break;
            }
          case 'zip':
            if (!isValidZip(form[field].value)) {
              lis.push(`<li>Enter the ZIP Code associated with the credit card.</li>`);
              break;
            }
          case 'terms':
            if (!isChecked(form[field].value)) {
              lis.push(`<li>Agree to the Terms &amp; conditions.</li>`);
              break;
            }
        }
        return lis
      });
      var lis = [];

    }
        //alert('validate');

    return {
      validate:validate,
      creditCardType:creditCardType
    };

    // function printError(str) {
    //   var err = document.getElementById('error');
    //   err.classList.add('error');
    //   err.innerHTML = str;
    // }
    //
    // function clearError() {
    //   var err = document.getElementById('error');
    //   err.innerHTML = '';
    //   err.classList.remove('error');
    // }

});
