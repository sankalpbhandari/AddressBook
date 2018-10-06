var $add_div;
var $ph_div;
var $date_div;
var num;
$(document).ready(function () {
    $add_div = $('#address_div').clone();
    $ph_div = $('#phone_div').clone();
    $date_div = $('#date_div').clone();
    num = 0;
});

function remove(elem) {
    temp = elem.parentNode;
    temp.parentNode.removeChild(temp)
}


function removeph(elem) {
    temp = elem.parentNode.parentNode;
    temp.parentNode.removeChild(temp)
}

function add_addfn() {
    console.log("Here");
    num++;
    var $cloned = $add_div.clone();
    $cloned.attr('id', $add_div.attr('id') + '_' + num);
    $(':not([id=""])', $cloned).each(function () {
        $(this).attr('id', $(this).attr('id') + '_' + num);
    });
    $cloned.appendTo('#address_div1');
}

function add_phfn() {
    console.log("Here");
    num++;
    var $cloned = $ph_div.clone();
    $cloned.attr('id', $ph_div.attr('id') + '_' + num);
    $(':not([id=""])', $cloned).each(function () {
        $(this).attr('id', $(this).attr('id') + '_' + num);
    });
    $cloned.appendTo('#phone_div1');
}

function add_datefn() {
    console.log("Here");
    num++;
    var $cloned = $date_div.clone();
    $cloned.attr('id', $date_div.attr('id') + '_' + num);
    $(':not([id=""])', $cloned).each(function () {
        $(this).attr('id', $(this).attr('id') + '_' + num);
    });
    $cloned.appendTo('#date_div1');
}