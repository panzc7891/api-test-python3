# -*- coding: utf-8 -*-
"""
Created on 2020-01-08
@author: panzhaochao
"""
from util.judgeStr import judgestr
from util.operationExcel import operationExcel
from base.TestRunner import testrunner
class CreateReport():
    #创建标题函数
    def title(self,titles):
        titles = '''
<!DOCTYPE html>
<html>
<head>
	<title>%s</title>
	<meta charset="utf-8" name="viewport" content="width=device-width, initial-scale=1.0" >
    <!-- 引入 Bootstrap -->
    <link href="https://cdn.bootcss.com/bootstrap/3.3.6/css/bootstrap.min.css" rel="stylesheet">
    <!-- HTML5 Shim 和 Respond.js 用于让 IE8 支持 HTML5元素和媒体查询 -->
    <!-- 注意： 如果通过 file://  引入 Respond.js 文件，则该文件无法起效果 -->
    <!--[if lt IE 9]>
     <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
     <script src="https://oss.maxcdn.com/libs/respond.js/1.3.0/respond.min.js"></script>
    <![endif]-->
    <style type="text/css">
        .hidden-detail,.hidden-tr{
            display:none;
        }
    </style>
</head>
<body>
'''%(titles)
        h1_title = '''<div class="row">
    <div class="col-md-4 col-md-offset-4" style='margin-left:3%;'>
        <h1>测试报告</h1>'''
        return titles+h1_title
     #设置测试背景和直接结果汇总
    def run_deltail(self,starttime,endtime,pass_num,fail_num):
        test_background = '''
        <table  class="table table-hover table-condensed">
            <tbody>
                <tr>
                    <td><strong>开始时间:</strong>  %s</td>
                </tr>
                 <tr>
                    <td><strong>开始时间:</strong>  %s</td>
                </tr>
                <tr>
                    <td><strong>用例总数:</strong>  %s</td>
                </tr>
                <tr>
                    <td><strong>成功数量:</strong>  %s</td>
                </tr>
                <tr style="color:red">
                    <td><strong>失败数量:</strong>  %s</td>
                </tr>
                <tr style="color:green">
                    <td><strong>通过率:</strong>  %.2f%%</td>
                </tr>
            </tbody>
        </table>
    </div>
</div>
        '''%(starttime,endtime,(pass_num+fail_num),pass_num,fail_num,(pass_num/(pass_num+fail_num)))

        return test_background
    def test_case_detail(self):
        case_detail = '''<div class="row" style="margin:60px">
    <div >
        <div class="btn-group" role="group" aria-label="...">
            <button type="button" id="check-all" class="btn btn-primary"><strong>所有用例<strong></button>
            <button type="button" id="check-success" class="btn btn-success"><strong>成功用例</button>
            <button type="button" id="check-danger" class="btn btn-danger"><strong>失败用例</button>
        </div>
        <table  class="table table-hover table-condensed table-bordered" style="word-wrap:break-word; word-break:break-all;">
            <thead>
                <tr bgcolor="#3399FF">
                    <td><strong>用例ID</td>
                    <td><strong>用例名称</td>
                    <td><strong>预期结果</td>
                    <td  width="50%%"><strong>实际结果</td>
                    <td><strong>是否通过</td>
                </tr>
                '''
        return case_detail
    #设置按键颜色
    def setcolor(self,color):
        if color == 'Pass':
            htl = '''<td><font color='green'>Pass</td>'''
        else:
            htl = '''<td><font color='red'>Fail</td>'''
        return htl
    #设置显示用例执行详情
    def details(self,clazz,id,name,ecpect,reslut,is_pass):
        detail = '''
         <tr class="case-tr %s">
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            %s
         </tr>
        '''%(clazz,id,name,ecpect,reslut,self.setcolor(is_pass))
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
    def case_data_detail(self):
       try:
           relus = ' '
           case_id = operationExcel().get_col_value(0)
           case_name = operationExcel().get_col_value(1)
           ecpect = operationExcel().get_col_value(10)
           resluts = operationExcel().get_col_value(11)
           ispass = operationExcel().get_col_value(12)
           #resluts = testrunner().run_main()[0]
           #ispass = testrunner().run_main()[1]
           for i in range(1,len(ispass)):
               if ispass[i] == 'Pass':
                   clazy = "success"
               elif ispass[i] == 'Fail':
                   clazy = "danger"
               else:
                   continue
               relus += self.details(clazy,case_id[i],case_name[i],ecpect[i],resluts[i],ispass[i])
           return relus
       except Exception as e:
           return ('读取执行用例详情信息失败：%s'%e)
    #创建测试报告
    def create_report_html(self,filenamepath,title,starttime,endtime):
        try:
            ispass = operationExcel().get_col_value(12)[1:]
            #ispass = testrunner().run_main()[1]
            pass_num = judgestr().judge_number(ispass,'Pass')
            fail_num = judgestr().judge_number(ispass,'Fail')
            text = self.title(title)+self.run_deltail(starttime,endtime,pass_num,fail_num)+self.test_case_detail()+self.case_data_detail()+self.details_click()
            with open(filenamepath,'w',encoding='utf-8') as f:
                f.write(text)
                f.close()
        except Exception as e:
            return ('创建测试报告失败：%s'%e)