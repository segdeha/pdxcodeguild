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
function isNotEmpty(value) {
  if (value !== null)
    return true
  else {
    return false
  }
}

function isValidName(value) {
  if (/^[a-zA-Z\s]*$/.test(value))
    return true
  else {
    return false
  }
}

function isValidCC(value) {
  if (/^(\d{16}\-?|\s?)$/|(/^(\d{15}\-?|\s)$/).test(value))
    return true
  else {
    return false
  }
}

function isValidCCV(value) {
  if (/^(\d{3})$/.test(value))
    return true
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
  if (value !== null)
    return true
  else {
    return false
  }
}

define(function () {
    function validate(form, requiredFields) {
      for (var i = 0; i < requiredFields.length; i++) {
        var value = (form[requiredFields[i]].value);
          isNotEmpty(value)
            if (true) {
              if (i = 'name')
                isValidName(value)
              else if (i = 'credit-card')
                isValidCC(value)
              else if (i = 'ccv')
                isValidCCV(value)
              else if (i = 'zip')
                isValidZip(value)
              else if (i = 'terms')
                isChecked(value)
            }
            else {
              printError()
            }

        }
      }
      // var name = form['i'].value
      // var creditCard = form['credit-card']
      // var ccv = form['ccv']
      // var zip = form['zip']
      // var agreetc = form['terms']
        // if (name = null);
        //   printError(0)
        // else if (name != null);
        //  return name = true

        //alert('validate');

    return validate;

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
