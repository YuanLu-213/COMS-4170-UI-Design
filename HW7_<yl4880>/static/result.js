function display(index, item){
    let result_row = $("<div class='row result'></div>");
    var id = item["id"]
    var image_link = $("<a href='/view/" + id + "'></a>")

    let col_1 = $("<div class='col-md-8'></div>");
    let res_img = $("<img class='result_img' src='" + item["image"] + "' alt='photo of " + item["name"] + "'>");
    image_link.html(res_img)
    col_1.append(image_link);
    result_row.append(col_1);

    var start = item["start"];
    var end = item["end"];

    let col_2 = $("<div class='col-md-4'></div>");
    let row_1 = $("<div class='row name'></div>");
    let res_name = $("<div id='result_name'></div>");

    let row_2 = $("<div class='row des'></div>");
    let car_type = $("<div id='result_type'></div>");

    let row_3 = $("<div class='row drive'></div>");
    let car_drive = $("<div id='result_drive'></div>");

    if (item["match"]=="name") {
        var name = item["name"];
        var name_hl = [name.slice(0, start), "<span class='highlight'>", name.slice(start, end), "</span>", name.slice(end)].join('');
        res_name.html(name_hl);
        car_type.html(item["type"]);
        car_drive.html(item["spec"][0]["drive"]);
        row_1.append(res_name)
        col_2.append(row_1);
        
        row_2.append(car_type);
        col_2.append(row_2);

        row_3.append(car_drive);
        col_2.append(row_3);

    result_row.append(col_2);
    } else if (item["match"]=="type"){
        res_name.html(item["name"]);
        var type = item["type"];
        var type_hl = [type.slice(0, start), "<span class='highlight'>", type.slice(start, end), "</span>", type.slice(end)].join('');
        car_type.html(type_hl);
        car_drive.html(item["spec"][0]["drive"]);
        row_1.append(res_name)
        col_2.append(row_1);
        
        row_2.append(car_type);
        col_2.append(row_2);
    
        row_3.append(car_drive);
        col_2.append(row_3);
    
        result_row.append(col_2);
    } else {
        res_name.html(item["name"]);
        car_type.html(item["type"]);
        var drive = item["spec"][0]["drive"];
        var drive_hl = [drive.slice(0, start), "<span class='highlight'>", drive.slice(start, end), "</span>", drive.slice(end)].join('');
        car_drive.html(drive_hl);
        row_1.append(res_name)
        col_2.append(row_1);
        
        row_2.append(car_type);
        col_2.append(row_2);
    
        row_3.append(car_drive);
        col_2.append(row_3);
    
        result_row.append(col_2);
    }
    console.log(car_drive);

    return result_row
}

$(document).ready(function(){
    if(results.length == 0){
        $("#show_result").empty();
        $("#num-results").empty();
        $("#show_result").html("No result found");
    }
    else{
        $("#show_result").empty();
        $("#result").empty();
        $("#num-results").empty();
        var num = results.length;
        $("#show_result").html("Showing Results for " + keyword);
        $("#num-results").html(num + " results found");
        $.each(results, function(index, item){

            var car = display(index, item);
    
            $("#result").append(car);
        });

    }
})