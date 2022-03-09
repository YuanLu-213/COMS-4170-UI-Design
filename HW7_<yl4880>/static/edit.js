function prepop() {
    var type = 0;
    var door = 0;
    var drive = 0;
    var fuel = 0;
    if (item["type"] == "SUV") {
        type = 1;
    } else if (item["type"] == "Sedan"){
        type = 2;
    } else{
        type = 3;
    }

    if (item["doors"] == "2") {
        door = 1;
    } else{
        door = 2;
    }

    if (item["spec"][0]["drive"] == "All Wheel Drive") {
        drive = 1;
    } else if (item["spec"][0]["drive"]== "Rear Wheel Drive"){
        drive = 2;
    } else{
        drive = 3;
    }

    if (item["spec"][0]["fuel"] == "Gasoline") {
        fuel = 1;
    } else if (item["spec"][0]["fuel"] == "Diesel"){
        fuel = 2;
    } else{
        fuel = 3;
    }


    $("#input-name").val(item["name"]);
    $("#car-type").val(type);
    $("#input-image").val(item["image"]);
    $("#input-highlight").val(item["highlight"]);
    $("#input-des").val(item["description"]);
    $("#input-price").val(item["price"]);
    $("#car-door").val(door);
    $("#car-drive").val(drive);
    $("#input-engine").val(item["spec"][0]["engine"]);
    $("#input-trans").val(item["spec"][0]["transmission"]);
    $("#car-fuel").val(fuel);

}

function  validation(){
    var valid = true;
    var image_url = $("#input-image").val().trim();
    var highlight_url = $("#input-highlight").val().trim();
    var car_description = $("#input-des").val().trim();
    var car_price = $("#input-price").val();
    var car_door = $("#car-door").val();
    var car_drive = $("#car-drive").val();
    var car_engine = $("#input-engine").val().trim();
    var car_trans = $("#input-trans").val().trim();
    var car_fuel = $("#car-fuel").val();

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
    var name = item["name"];

    $( "#dialog-confirm" ).dialog({
        autoOpen: false,
        resizable: false,
        height: "auto",
        width: 400,
        modal: true,
        buttons: {
          "Discard Changes": function() {
            $( this ).dialog( "close" );
            window.location.href = "/view/" + item["id"];
          },
          Cancel: function() {
            $( this ).dialog( "close" );
          }
        }
    });

    $("#edit-car").html("Edit " + name);
    prepop();

    $("#edit-form").submit(function(event){
        event.preventDefault();
        $(".form-control").removeClass("is-invalid");
        $(".invalid-feedback").empty();

        var validated = validation();
        if (validated == true){
            var car_id = item["id"];
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

            var edited = {
                "id": car_id,
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
                url: "/edit_car",
                dataType: "json",
                contentType: "application/json; charset=utf-8",
                data: JSON.stringify(edited),
                success: function(res){
                    console.log("success")
                    window.location.href = "/view/" + edited["id"]
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

    $("#discard").click(function(event){
        event.preventDefault();
        $( "#dialog-confirm" ).dialog("open", {
            resizable: false,
            height: "auto",
            width: 400,
            modal: true,
            buttons: {
              "Discard Changes": function() {
                $( this ).dialog( "close" );
                window.location.href = "/view/" + item["id"];
              },
              Cancel: function() {
                $( this ).dialog( "close" );
              }
            }
        });
    })
})