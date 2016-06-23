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
  if (value !== "")
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
  if (/^3/) {
    cc_type =
    if ((/^(\d{15}\-?|\s)$/).test(value))
      return true
    else {
      return false
    }
  }
  if ((/^4/)|(/^5/)|(/^6/)) {
    if ((/^(\d{16}\-?|\s?)$/).test(value))
      return true
    else {
      return false
    }
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
  if (value !== "")
    return true
  else {
    return false
  }
}

define(function () {
    function validate(form, requiredFields) {
      var html ;
      var isok = true;
      var cc_type ;
      requiredFields.forEach(function(field) {
        switch(field) {
          case 'name':
            if (!isValidName(form[field].value)) {
              isok = false;
              break;
            }
          case 'credit-card':
            if (!isValidCC(form[field].value)) {
              isok = false;
              break;
            }
          case 'ccv':
            if (!isValidCCV(form[field].value)) {
              isok = false;
              break;
            }
          case 'zip':
            if (!isValidZip(form[field].value)) {
              isok = false;
              break;
            }
          case 'terms':
            if (!isChecked(form[field].value)) {
              isok = false;
              break;
            }
        }
      });
      // for (var i = 0; i < requiredFields.length; i++) {
      //   var value = (form[requiredFields[i]].value);
      //     isNotEmpty(value)
      //       if (true) {
      //         if (requiredFields[i] === 'name')
      //           isValidName(value)
      //         else if (requiredFields[i] === 'credit-card')
      //           isValidCC(value)
      //         else if (requiredFields[i] === 'ccv')
      //           isValidCCV(value)
      //         else if (requiredFields[i] === 'zip')
      //           isValidZip(value)
      //         else if (requiredFields[i] === 'terms')
      //           isChecked(value)
      //       }
      //       return
      //       else {
      //         printError()
      //       }
      //
      //   }
      }
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
