angular.
  module('phonecatApp').
  component('phoneList', {
    templateUrl: 'phone-list/phone-list.template.html',
    controller: [ '$http',
        function PhoneListController($http) {
            var self = this;
            $http.get('/proxy/webapp/phonelist').then(function(response) {
                self.phones = response.data;
                console.log(self.phones)
            });
        }
    ]
  });
