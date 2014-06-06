/*
 * index.js
 * Copyright (C) 2014 george <george@george-VirtualBox>
 *
 * Distributed under terms of the MIT license.
 */



function CodeController($scope){
    $scope.items = [];
    $scope.refresh = function(){
        bigdatalab.gpcode.list({}).execute(function(data){
            // http://stackoverflow.com/questions/20599877/angularjs-ngrepeat-update-model
            $scope.items = data['items'];
            $scope.$apply();
        })
    }
    $scope.get = function(code_id){
        bigdatalab.gpcode.get({"id": code_id}).execute(function(data){
            $scope.exec_code = data['exec_code'];
            $scope.eval_code = data['eval_code'];
            $scope.id = data['id'];
            $scope.name = data['name'];
            $scope.$apply();
        })
    }
    $scope.send = function(){
        var data = {
            'exec_code': $scope.exec_code,
            'eval_code': $scope.eval_code,
            'name': $scope.name
        };
        if($scope.id){
            data['id'] = $scope.id;
            bigdatalab.gpcode.update(data).execute(function(data){})
        }else{
            bigdatalab.gpcode.insert(data).execute(function(data){
                $scope.id = data['id'];
                $scope.refresh();
            })
        }
    }
    $scope.new = function(){
        $scope.id = "";
        $scope.exec_code = "";
        $scope.eval_code = "";
        $scope.name = "";
        $scope.$apply();
    }
}


(function(){
    var bigdatalab;
    var ROOT = '/_ah/api';
    var init = function(){
        // initialize bigdatalab module
        gapi.client.load('bigdatalab', 'v1', function() {
            window.bigdatalab = gapi.client.bigdatalab;
            angular.element(document.getElementById('code')).scope().refresh();
        }, ROOT);
        
    }

    window.init = init;


}())
