/*jshint browser: true, nomen: false, eqnull: true, es5:true, trailing:true */


(function ($) {
  $(document).ready(function () {
    var addView = '++add++collective.talkflow.discussion';
    console.log('Talkflow ready');
    if (window.location.pathname.indexOf(addView) !== -1) {
      if (window.location.search.indexOf('addquestion') !== -1) {
        console.log('Add a question');
        $('#form-widgets-question-0').prop( "checked", true );
        $('h1.documentFirstHeading').text('Add a Question to Discuss');
        $('#formfield-form-widgets-IBasic-title label')
          .append(
            $('<span>(short version of question)</span>')
          );
        $('#formfield-form-widgets-question').hide();
      }
    }
  });
}(jQuery));

