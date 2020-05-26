import xlsxwriter
class CreateReport():
    #创建标题函数
    def title(self,titles):
        titles = '''
<!DOCTYPE html>
<html>
<head>
    <title>%s</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.bootcss.com/bootstrap/3.3.6/css/bootstrap.min.css" rel="stylesheet">
    <style type="text/css">
        .hidden-detail,.hidden-tr{
            display:none;
        }
    </style>
</head>
<body>
'''%(titles)
        h1_title = '''<div  class='col-md-4 col-md-offset-4' style='margin-left:3%;'>
<h1>接口测试结果</h1>
'''
        return titles+h1_title

     #设置测试背景和直接结果汇总
    def run_deltail(self,starttime,endtime,total,pass_num,fail_num):
        test_background = '''
      <table  class="table table-hover table-condensed">
        <tbody>
            <tr>
                <td><strong>开始时间:</strong> %s</td></tr>
                <td><strong>结束时间:</strong> %s</td></tr>
                <td><strong>执行耗时:</strong> %s</td></tr>
                <td><strong>测试结果:</strong><span >用例总数: <strong >%s</strong>
                            通过: <strong >%s</strong>
                            失败: <strong >%s</strong>
                            通过率: <strong >%s</strong>
                            </span></td></tr>
        </tbody></table>
        </div> 
        '''%(starttime,endtime,10,total,pass_num,fail_num,(pass_num/total))

        return test_background
    def test_case_detail(self):
        case_detail = '''<div class="row " style="margin:60px">
                    <div style='    margin-top: 18%;' >
                    <div class="btn-group" role="group" aria-label="...">
                        <button type="button" id="check-all" class="btn btn-primary">所有用例</button>
                        <button type="button" id="check-success" class="btn btn-success">成功用例</button>
                        <button type="button" id="check-danger" class="btn btn-danger">失败用例</button>
                    </div>
                    <div class="btn-group" role="group" aria-label="...">
                    </div>
                    <table class="table table-hover table-condensed table-bordered" style="word-wrap:break-word; word-break:break-all;  margin-top: 7px;">
                    <tr >
                        <td><strong>用例ID&nbsp;</strong></td>
                        <td><strong>用例名字&nbsp;</strong></td>
                        <td><strong>预期结果&nbsp;</strong></td>
                        <td><strong>实际结果&nbsp;</strong></td>  
                        <td><strong>是否通过&nbsp;</strong></td>
                    </tr>
                '''
        return case_detail
    #设置按键颜色
    def setcolor(self,color):
        if color == 'pass':
            htl = '''<td bgcolor="green">pass</td>'''
        else:
            htl = '''<td bgcolor="fail">fail</td>'''
        return htl
    #设置显示用例执行详情
    def details(self,id,name,ecpect,reslut,is_pass):
        detail = '''
         <tr class="case-tr %s">
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
         </tr>
        '''%(id,name,ecpect,reslut,self.setcolor(is_pass))
        return detail

    #设置用例执行详情标题点击后内容显示
    def details_click(self):
        footing = '''</div></div></table><script src="https://code.jquery.com/jquery.js"></script>
<script src="https://cdn.bootcss.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
<script type="text/javascript">
    $("#check-danger").click(function(e){
        $(".case-tr").removeClass("hidden-tr");
        $(".success").addClass("hidden-tr");
    });
    $("#check-success").click(function(e){
        $(".case-tr").removeClass("hidden-tr");
        $(".danger").addClass("hidden-tr");
    });
    $("#check-all").click(function(e){
        $(".case-tr").removeClass("hidden-tr");
    });
</script>
</body></html>'''
        return footing
    def create_report_html(self,filenamepath,title,starttime,endtime,total,pass_num,fail_num,id,name,ecpect,reslut,is_pass):
        text = self.title(title)+self.run_deltail(starttime,endtime,total,pass_num,fail_num)+self.test_case_detail()+self.details(id,name,ecpect,reslut,is_pass)+self.details_click()
        with open(filenamepath,'wb') as f:
            f.write(text.encode('UTF-8'))
            f.close()

if __name__ == '__main__':
    filenamepath = r'D:\PyCharmProject\api-test-python3\report\report.html'
    title = '接口测试报告'
    starttime = '2020-05-25 15:03:33'
    endtime = '2020-05-25 15:33:33'
    total = 14
    pass_num = 10
    fail_num = 4
    id = 1
    name = 'wang'
    ecpect = 'wang'
    reslut = 'wang'
    is_pass = 'pass'
    CreateReport().create_report_html(filenamepath,title,starttime,endtime,total,pass_num,fail_num,id,name,ecpect,reslut,is_pass)
