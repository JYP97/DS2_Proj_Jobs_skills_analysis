from nameko_http import api
import json


class NamekoService:
    name = 'yyds'

    @api('POST', '/skill', cors_enabled=True)
    def skill(self, req):
        ''' input data has been decoded as 'request', please assign the output data to 'resp' '''

        request_str = req.data.decode('utf-8', errors='ignore')
        request = eval(request_str)['request']

        ''' check request data '''
        # print('print: == request ==')
        # print(request)
        # print(type(request))
        # print('print: ----')

        ''' [your code] '''
#         output = SkillJobmatcher(request, num_jobs, method).method
        ''' test resp data '''
#         resp = 's1,s2,s3,s4,s5,s6,s7,s8,s9,10'
        output = ['3D Modeler -CAD', 'Logistics Analyst', 'Powertrain Software Engineer', 'Reading Specialist - ESY', 'Senior Software Engineer - Customer Care Self-Service', 'CRM / PHP Developer', 'Backend Java Developer', 'Software Developer', 'IT Business Analyst', 'Software Developer to Salesforce: Paid Training/FT Opportunity']
        output = (','.join(output))

        ''' test resp data '''
        print('print: == response ==')
        resp = output
        dict = {'request': request, 'response': resp}
        print(dict)
        print('print: ----')

        return json.dumps({'response': resp})

    @api('POST', '/job', cors_enabled=True)
    def job(self, req):
        ''' input data has been decoded as 'request', please assign the output data to 'resp' '''

        request_str = req.data.decode('utf-8', errors='ignore')
        request = eval(request_str)['request']

        ''' check request data '''
        print('print: == request ==')
        print(request)
        print(type(request))
        print('print: ----')

        ''' [your code] '''

        output = {'Title': 'CRM / PHP Developer',
                  'Description': 'We are looking for a CRM developer to join our IT team! As a CRM Developer, you will be responsible for the server-side web application logic as well as for the integration of the front-end part.',
                  'Skills': 'PHP (Scripting Language), Debugging, Web Services, JSON, Symfony, Simple Object Access Protocol (SOAP), Troubleshooting (Problem Solving), Testing, User Interface, Front End (Software Engineering)',
                  'Company': 'ExecuSource',
                  'Locality': 'Duluth',
                  'Address': '1814 Atrium Place Drive',
                  'Salary': '$106,250.00 - $125,000.00 / year'}

        ''' test resp data '''
        print('print: == response ==')
        resp = output
        dict = {'request': request, 'response': resp}
        print(dict)
        print('print: ----')

        return json.dumps({'response': resp})
