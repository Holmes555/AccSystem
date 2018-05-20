function select_all() {
    if($('#select_all').prop('checked')) {
        $('.chbox').prop('checked', true);
        $('#del_btn').removeClass('invisible');
    }
    else {
        $('.chbox').prop('checked', false);
        $('#del_btn').addClass('invisible');
    }
}

function select_job() {

    if(jQuery('#select_form input[type=checkbox]:checked').length > 0) {
        $('#del_btn').removeClass('invisible');
    }
    else {
        $('#del_btn').addClass('invisible');
    }
}

function delete_reports() {
    var jobs = [];
    $('.chbox:checkbox:checked').each(function() {
        jobs.push($(this).val());
    });
    $.get('../delete_reports/', {job_list: jobs}, function (response) {
        $('#reports_table').show().html(response);
        $('#del_btn').addClass('invisible');
    });
}
