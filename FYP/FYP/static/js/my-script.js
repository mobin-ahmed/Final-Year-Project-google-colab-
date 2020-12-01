// var xydata=[1,2,3,4,5,6];
        var xx=[];
        var yy=[];
        const canvas=document.querySelector("#canvas");
        const ctx=canvas.getContext("2d");

        // canvas.height=window.innerHeight*0.3;
        // canvas.width=window.innerWidth*0.3;

        // ctx.fillRect(100,100,200,200);

        let painting=false;

        function startPosition(e){
            painting=true;
            draw(e);
        }

        function finishedPosition(){
            painting=false;
            ctx.beginPath()
        }

        function draw(e){
            if(!painting) return;
            ctx.linrWidth=10;
            ctx.lineCap="round";
            ctx.strokeStyle="white";

            // arr1.push(e.clientX);
            // arr2.push(e.clientY);
            var x=e.clientX;
            var y=e.clientY;

            xx.push(x);
            yy.push(y);

            ctx.lineTo(e.clientX,e.clientY);
            ctx.stroke();
            ctx.beginPath();
            ctx.moveTo(e.clientX,e.clientY);

        }

        canvas.addEventListener("mousedown",startPosition);
        canvas.addEventListener("mouseup",finishedPosition);
        canvas.addEventListener("mousemove",draw);




        
// Set up touch events for mobile, etc
        canvas.addEventListener("touchstart", function (e) {
            mousePos = getTouchPos(canvas, e);
            var touch = e.touches[0];
            var mouseEvent = new MouseEvent("mousedown", {
                clientX: touch.clientX,
                clientY: touch.clientY
            });
            canvas.dispatchEvent(mouseEvent);
        }, true);
        canvas.addEventListener("touchend", function (e) {
            var mouseEvent = new MouseEvent("mouseup", {});
            canvas.dispatchEvent(mouseEvent);
        }, true);
        canvas.addEventListener("touchmove", function (e) {
            var touch = e.touches[0];
            var mouseEvent = new MouseEvent("mousemove", {
                clientX: touch.clientX,
                clientY: touch.clientY
            });
            canvas.dispatchEvent(mouseEvent);
        }, true);

        // Prevent scrolling when touching the canvas
        document.body.addEventListener("touchstart", function (e) {
            if (e.target == canvas) {
                e.preventDefault();
            }
        }, true);
        document.body.addEventListener("touchend", function (e) {
            if (e.target == canvas) {
                e.preventDefault();
            }
        }, true);
        document.body.addEventListener("touchmove", function (e) {
            if (e.target == canvas) {
                e.preventDefault();
            }
        }, true);

        // Get the position of the mouse relative to the canvas
        function getMousePos(canvasDom, mouseEvent) {
            var rect = canvasDom.getBoundingClientRect();
            return {
                x: mouseEvent.clientX - rect.left,
                y: mouseEvent.clientY - rect.top
            };
        }

        // Get the position of a touch relative to the canvas
        function getTouchPos(canvasDom, touchEvent) {
            var rect = canvasDom.getBoundingClientRect();
            return {
                x: touchEvent.touches[0].clientX - rect.left,
                y: touchEvent.touches[0].clientY - rect.top
            };
        }

    // var xy_merge=xx.concat(yy);

    // console.log(xx);
    // console.log(yy);

   


$("#pushBtn").click(function(e){

    var dt1=JSON.stringify(xx);
    var dt2=JSON.stringify(yy);
    //console.log('dt='+dt);
    var name=$("#p").val();
    console.log(name)
    $.ajax({
        url:'/saveData',
        type: 'POST',
        data:{
            'x':dt1,
            'y':dt2,
            'name':name
        },
        success: function(response){
            // console.log(response);
            window.alert("data recive succesfully");
            location.reload();
        },
        error: function(error){
            // console.log(error);
            window.alert("data recive failed");
            location.reload();
        }
    });
    e.preventDefault();
})

    $("#refBtn").click(function(){
        location.reload();
    });