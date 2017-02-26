function select_all_employees(){
    // 全选
    var select_status = document.getElementById("select_all").checked;
    var all_employees = $('.employee');
    for(var m=0; m<all_employees.length; m++){
        all_employees[m].checked = select_status;
    }
}


function change_on_employees() {
    var emp_ids = "";
    var select_emps = $('.employee');
    for(var m=0; m<select_emps.length; m++){
        if(select_emps[m].checked == true) {
            var emp_id = select_emps[m].getAttribute('data-target');
            emp_ids = emp_ids + emp_id + ','
        }
    }
    if (emp_ids == ""){
        return
    }

    var train_id = $("#title").data('target');

    $.ajax({
        url: '/admimlte/train/employee/'+ train_id +'/batch/',
        type: 'POST',
        data: {"emp_ids": emp_ids, "flag": "on"},
        success: function (result) {
            if (result.code == 0){
                window.location.reload();
                var select_emps = $('.employee');
                for(var m=0; m<select_emps.length; m++){
                    select_emps[m].checked = false;
                }
                document.getElementById("select_all").checked = false;
            }else{
                alert(result.message);
            }
        }
    });
}


function change_off_employees() {
    var emp_ids = "";
    var select_emps = $('.employee');
    for(var m=0; m<select_emps.length; m++){
        if(select_emps[m].checked == true) {
            var emp_id = select_emps[m].getAttribute('data-target');
            emp_ids = emp_ids + emp_id + ','
        }
    }
    if (emp_ids == ""){
        return
    }

    var train_id = $("#title").data('target');

    $.ajax({
        url: '/adminlte/train/employee/'+ train_id +'/batch/',
        type: 'POST',
        data: {"emp_ids": emp_ids, "flag": "off"},
        success: function (result) {
            if (result.code == 0){
                window.location.reload();
                var select_emps = $('.employee');
                for(var m=0; m<select_emps.length; m++){
                    select_emps[m].checked = false;
                }
                document.getElementById("select_all").checked = false;
            }else{
                alert(result.message);
            }
        }
    });
}


function delete_salary(e){
    var salary_id = e.getAttribute('data-target');
    $.ajax({
        url: 'salary/' + salary_id + '/delete/',
        type: 'POST',
        data: {},
        success: function (result) {
            if (result.code == 0){
                window.location = '/salary';
            }else{
                alert(result.message);
            }
        }
    });
}
