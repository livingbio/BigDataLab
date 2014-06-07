/*
 * index.js
 * Copyright (C) 2014 george <george@george-VirtualBox>
 *
 * Distributed under terms of the MIT license.
 */



function CodeController($scope){
    $scope.items = [];
    $scope.refresh = function(){
        setTimeout(
            function(){
                bigdatalab.gpcode.list({}).execute(function(data){
                    // http://stackoverflow.com/questions/20599877/angularjs-ngrepeat-update-model
                    $scope.items = data['items'];
                    $scope.$apply();
                    console.log('refreshed')
                })
            }
        , 500)
    }
    $scope.get = function(item){
        bigdatalab.gpcode.get({"id": item.id}).execute(function(data){
            var exec_code = $("#exec_code").data("code");
            var eval_code = $("#eval_code").data("code");
            exec_code.setValue(data['exec_code']);
            eval_code.setValue(data['eval_code']);
            $scope.id = data['id'];
            $scope.name = data['name'];
            $scope.$apply();
            console.log('getted')
        })
    }
    $scope.send = function(){
        var exec_code = $("#exec_code").data("code");
        var eval_code = $("#eval_code").data("code");
        var data = {
            'exec_code': exec_code.getValue(),
            'eval_code': eval_code.getValue(),
            'name': $scope.name
        };
        if($scope.id){
            data['id'] = $scope.id;
            bigdatalab.gpcode.update(data).execute(function(data){
                $scope.refresh();
                console.log('updated')
            })
        }else{
            bigdatalab.gpcode.insert(data).execute(function(data){
                $scope.id = data['id'];
                $scope.refresh();
                console.log('added')
            })
        }
    }
    $scope.clean = function(){
        var exec_code = $("#exec_code").data("code");
        var eval_code = $("#eval_code").data("code");
        $scope.id = "";
        $scope.exec_code = "";
        $scope.eval_code = "";
        $scope.name = "";
        exec_code.setValue("");
        eval_code.setValue("");
        console.log('clean')
    }

    $scope.new = function(){
        $scope.clean()
        console.log('new');
    }
    $scope.remove = function(){
        bigdatalab.gpcode.delete({"id":$scope.id}).execute(function(data){
            $scope.new();
            console.log('removed')
            $scope.refresh();
        })
    }
}


(function(){
    var bigdatalab;
    var ROOT = '/_ah/api';
    var init = function(){
        // initialize bigdatalab module
        //
        gapi.client.load('bigdatalab', 'v1', function() {
            window.bigdatalab = gapi.client.bigdatalab;
            angular.element(document.getElementById('code')).scope().refresh();
        }, ROOT);



        var exec_code = CodeMirror.fromTextArea($("#exec_code")[0], { value: "", mode:  "python", lineNumbers: true, gutters: ["CodeMirror-linenumbers", "breakpoints"]});
        var eval_code = CodeMirror.fromTextArea($("#eval_code")[0], { value: "", mode:  "python", lineNumbers: true, gutters: ["CodeMirror-linenumbers", "breakpoints"]});
        $("#exec_code").data("code", exec_code);
        $("#eval_code").data("code", eval_code);
        
    }

    window.init = init;


}())
