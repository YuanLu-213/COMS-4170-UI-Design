function existed(car_name, names){
    $.each(names, function(index, item){
        if (car_name.toLowerCase() == item.toLowerCase()){
            return true
        }
    })

    return false
}

function  validation(){
    var valid = true;
    var car_name = $("#input-name").val().trim();
    var car_type = $("#car-type").val();
    var image_url = $("#input-image").val().trim();
    var highlight_url = $("#input-highlight").val().trim();
    var car_description = $("#input-des").val().trim();
    var car_price = $("#input-price").val();
    var car_door = $("#car-door").val();
    var car_drive = $("#car-drive").val();
    var car_engine = $("#input-engine").val().trim();
    var car_trans = $("#input-trans").val().trim();
    var car_fuel = $("#car-fuel").val();

    
    if (existed(car_name, names)) {
        $("#input-name").addClass("is-invalid");
        $(".name").html(car_name + " already existed in our system");
        valid = false;
    } else {
        if (car_name.length == 0) {
            $("#input-name").addClass("is-invalid");
            $(".name").html("Please fill in a valid make model");
            valid = false;
        } else if(car_name.replace(/\s+/g, "").length == 0){
            $("#input-name").addClass("is-invalid");
            $(".name").html("Make Model cannot be empty");
            valid = false;
        }
    }

    if (car_type == 0){
        $("#car-type").addClass("is-invalid");
        $(".type").html("Please select a type");
        valid = false;
    }

    if (image_url.length == 0){
        $("#input-image").addClass("is-invalid");
        $(".image").html("Please fill in a valid URL");
        valid = false;
    } else if(image_url.replace(/\s+/g, "").length == 0){
        $("#input-image").addClass("is-invalid");
        $(".image").html("Image URL cannot be empty");
        valid = false;
    }

    if (highlight_url.length == 0){
        $("#input-highlight").addClass("is-invalid");
        $(".highlight").html("Please fill in a valid URL");
        valid = false;
    } else if(highlight_url.replace(/\s+/g, "").length == 0){
        $("#input-highlight").addClass("is-invalid");
        $(".highlight").html("Image URL cannot be empty");
        valid = false;
    }

    if (car_description.length == 0) {
        $("#input-des").addClass("is-invalid");
        $(".des").html("Please fill in a description");
        valid = false;
    } else if(car_description.replace(/\s+/g, "").length == 0){
        $("#input-des").addClass("is-invalid");
        $(".des").html("Description cannot be empty");
        valid = false;
    }

    if (car_price.replace(/\s+/g, "").length == 0) {
        $("#input-price").addClass("is-invalid");
        $(".price").html("Please fill in a valid price");
        valid = false;
    } else {
        var price = Number(car_price);     
        if (Number.isNaN(price) || (!Number.isInteger(price))) {
            $("#input-price").addClass("is-invalid");
            $(".price").html("Please fill in an integer number");
            valid = false;
        }
    }

    if (car_door == 0){
        $("#car-door").addClass("is-invalid");
        $(".door").html("Please select number of doors");
        valid = false;
    }

    if (car_drive == 0){
        $("#car-drive").addClass("is-invalid");
        $(".drive").html("Please select drive system");
        valid = false;
    }

    if (car_engine.length == 0) {
        $("#input-engine").addClass("is-invalid");
        $(".engine").html("Please fill in a valid engine");
        valid = false;
    } else if(car_engine.replace(/\s+/g, "").length == 0){
        $("#input-engine").addClass("is-invalid");
        $(".engine").html("Engine cannot be empty");
        valid = false;
    }

    if (car_trans.length == 0) {
        $("#input-trans").addClass("is-invalid");
        $(".trans").html("Please fill in a valid transmission");
        valid = false;
    } else if(car_trans.replace(/\s+/g, "").length == 0){
        $("#input-trans").addClass("is-invalid");
        $(".trans").html("Transmission cannot be empty");
        valid = false;
    }

    if (car_fuel == 0){
        $("#car-fuel").addClass("is-invalid");
        $(".fuel").html("Please select fuel type");
        valid = false;
    }

    return valid
}

$(document).ready(function(){
    $("#add-form").submit(function(event){
        event.preventDefault();

        $("#success").empty();
        $(".form-control").removeClass("is-invalid");
        $(".invalid-feedback").empty();

        var validated = validation();
        console.log(validated)
        if (validated == true){
            var car_name = $("#input-name").val().trim();
            var car_type = $("#car-type option:selected").text();
            var image_url = $("#input-image").val().trim();
            var highlight_url = $("#input-highlight").val().trim();
            var car_description = $("#input-des").val().trim();
            var car_price = $("#input-price").val();
            var car_door = $("#car-door option:selected").text();
            var car_drive = $("#car-drive option:selected").text();
            var car_engine = $("#input-engine").val().trim();
            var car_trans = $("#input-trans").val().trim();
            var car_fuel = $("#car-fuel option:selected").text();
            console.log(car_price);

            var added = {
                "name": car_name,
                "type": car_type,
                "image": image_url,
                "highlight": highlight_url,
                "description": car_description,
                "price": parseInt(car_price),
                "doors": parseInt(car_door),
                "spec": [
                    {
                        "drive": car_drive,
                        "engine": car_engine,
                        "transmission": car_trans,
                        "fuel":car_fuel,
                    }
                ]
            }

            $.ajax({
                type: "POST",
                url: "add_car",
                dataType: "json",
                contentType: "application/json; charset=utf-8",
                data: JSON.stringify(added),
                success: function(res){
                    $("#success").empty();
                    $("#success").html("You have successfully added a car");
                    var new_car = $("<a id='new_car' href='" + res["url"] + "'>See it here</a>");
                    $(".succeed").append(new_car);
                    $(".form-control").val("");
                    $("#input-name").focus();
                },
                error: function(request, status, error){
                    console.log("Error");
                    console.log(request)
                    console.log(status)
                    console.log(error)
                }
            })
        }
    })
})