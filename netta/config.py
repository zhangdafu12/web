# coding:utf-8
# _author_:Junjie
# date:2018/10/19

# 请求头
command_head = {
    'send_search_task': 'Search_task',
    'response_search_task': 'Ack_Search_task',
    'response_command': 'Ack_command_task',
    'send_search_result': 'Search_result',
    'response_search_result': 'Ack_result',
    'send_search_task_request': 'Search_task_request',
    'no_node':'busy',
    'response_no_task': 'No_task',
    'task_finish': 'Task_finished',
    'command_error': 'error',

    'simnode_task_request': 'simComputing_task_request',
    'send_sim_task': 'simComputing_task',
    'response_sim_task': 'Ack_simComputing_task',
    'send_sim_result': 'simComputing_result',
    'response_sim_result': 'Ack_simComputing_result',
    'send_task_to_sendsimnode': 'simComputing_task',
    'response_sendsimnode_task': 'Ack_simComputing_task',
    'response_sendsimnode_result': 'Ack_simComputing_result',
    'take_sim_result':'take_sim_result',
    'final_sim_result':'final_sim_result',

    'textparsenode_task_request':'textparsenode_task_request',
    'send_textparse_task':'textparse_task',
    'response_textparse_task':'Ack_textparse_task',
    'send_textparse_result':'send_textparse_result',
    'response_textparse_result':'Ack_textparse_result',
    'take_search_result':'take_search_result',
    'final_search_result':'final_search_result',
    'take_textparse_result':'take_textparse_result',
    'final_textparse_result':'final_textparse_result',

    'deal_task_request':'dealnode_task_request',# 任务请求标志头，表示一个任务节点对总控汇报自己空闲，任务节点--->总控
    'send_deal_task':'deal_task',# 任务消息标志头，先从本地发至总控，总控再发至任务节点    本地--->总控--->任务节点，表明发过来的是待执行的任务
    'response_deal_task':'Ack_deal_task',# 任务节点回应总控节点，表明自己受到了任务内容    任务节点--->总控
    'send_deal_result':'send_deal_result',#任务节点向总控发送任务执行结果，   任务节点--->总控
    'response_deal_result':'Ack_deal_result',# 总控节点向任务节点发送收到执行结果的确认消息   ，总控--->任务节点
    'take_deal_result':'take_deal_result',# 本地节点向总控请求任务结果，本地---->总控，总控相当于本地节点的代理，总控发出的任务请求，事实上来源于本地
    'final_deal_result':'final_deal_result',# 总控相本地节点返回任务结果  ，总控--->本地节点

    'image_task_request':'imagenode_task_request',
    'send_image_task':'image_task',
    'response_image_task':'Ack_image_task',
    'send_image_result':'send_image_result',
    'response_image_result':'Ack_image_result',
    'take_image_result':'take_image_result',
    'final_image_result':'final_image_result',

    'linkedin_task_request':'linkedin_task_request',
    'send_linkin_task':'send_linkin_task',
    'response_linkin_task':'response_linkin_task',
    'send_linkin_result':'send_linkin_result',
    'response_linkin_result':'response_linkin_result',
    'take_linkin_result':'take_linkin_result',
    'final_linkin_result':'final_linkin_result',

    'whois_task_request':'whois_task_request',
    'send_whois_task':'send_whois_task',
    'response_whois_task':'response_whois_task',
    'send_whois_result':'send_whois_result',
    'response_whois_result':'response_whois_result',
    'take_whois_result':'take_whois_result',
    'final_whois_result':'final_whois_result',

    'checkmate_task_request':'checkmate_task_request',
    'send_checkmate_task':'send_checkmate_task',
    'response_checkmate_task':'response_checkmate_task',
    'send_checkmate_result':'send_checkmate_result',
    'response_checkmate_result':'response_checkmate_result',
    'take_checkmate_result':'take_checkmate_result',
    'final_checkmate_result':'final_checkmate_result',

    'domain_task_request':'domain_task_request',
    'send_domain_task':'send_domain_task',
    'response_domain_task':'response_domain_task',
    'send_domain_result':'send_domain_result',
    'response_domain_result':'response_domain_result',
    'take_domain_result':'take_domain_result',
    'final_domain_result':'final_domain_result',

    'beenverified_task_request':'beenverified_task_request',
    'send_beenverified_task':'send_beenverified_task',
    'response_beenverified_task':'response_beenverified_task',
    'send_beenverified_result':'send_beenverified_result',
    'response_beenverified_result':'response_beenverified_result',
    'take_beenverified_result':'take_beenverified_result',
    'final_beenverified_result':'final_beenverified_result',

    'qqSpider_task_request':'qqSpider_task_request',
    'send_qqSpider_task':'send_qqSpider_task',
    'response_qqSpider_task':'response_qqSpider_task',
    'send_qqSpider_result':'send_qqSpider_result',
    'response_qqSpider_result':'response_qqSpider_result',
    'take_qqSpider_result':'take_qqSpider_result',
    'final_qqSpider_result':'final_qqSpider_result',

    'facebook_task_request': 'facebook_task_request',
    'send_facebook_task': 'send_facebook_task',
    'response_facebook_task': 'response_facebook_task',
    'send_facebook_result': 'send_facebook_result',
    'response_facebook_result': 'response_facebook_result',
    'take_facebook_result': 'take_facebook_result',
    'final_facebook_result': 'final_facebook_result',

    'wechat_task_request': 'wechat_task_request',
    'send_wechat_task': 'send_wechat_task',
    'response_wechat_task': 'response_wechat_task',
    'send_wechat_result': 'send_wechat_result',
    'response_wechat_result': 'response_wechat_result',
    'take_wechat_result': 'take_wechat_result',
    'final_wechat_result': 'final_wechat_result',

    'search2_task_request': 'search2_task_request',
    'send_search2_task': 'send_search2_task',
    'response_search2_task': 'response_search2_task',
    'send_search2_result': 'send_search2_result',
    'response_search2_result': 'response_search2_result',
    'take_search2_result': 'take_search2_result',
    'final_search2_result': 'final_search2_result',

    # 针对事件及实体,实体关系提取的处理节点封装协议,简称 evtrelner evtrelner
    'evtrelner_task_request':'evtrelnernode_task_request',# 任务请求标志头，表示一个任务节点对总控汇报自己空闲，任务节点--->总控
    'send_evtrelner_task':'evtrelner_task',# 任务消息标志头，先从本地发至总控，总控再发至任务节点    本地--->总控--->任务节点，表明发过来的是待执行的任务
    'response_evtrelner_task':'Ack_evtrelner_task',# 任务节点回应总控节点，表明自己受到了任务内容    任务节点--->总控
    'send_evtrelner_result':'send_evtrelner_result',#任务节点向总控发送任务执行结果，   任务节点--->总控
    'response_evtrelner_result':'Ack_evtrelner_result',# 总控节点向任务节点发送收到执行结果的确认消息   ，总控--->任务节点
    'take_evtrelner_result':'take_evtrelner_result',# 本地节点向总控请求任务结果，本地---->总控，总控相当于本地节点的代理，总控发出的任务请求，事实上来源于本地
    'final_evtrelner_result':'final_evtrelner_result',# 总控相本地节点返回任务结果  ，总控--->本地节点

    'send_nlp_task':'nlp_task',
    'response_nlp_task':'Ack_nlp_task',
    'take_nlp_result':'take_nlp_result',
    'final_nlp_result':'final_nlp_result',
    'nlp_task_request':'nlp_task_request',
    'send_nlp_result':'send_nlp_result',
    'response_nlp_result':'response_nlp_result',

    # 今日头条
    'send_jinri_task_1':'jinri_task_1',
    'response_jinri_task_1':'Ack_jinri_task_1',
    'take_jinri_result_1':'take_jinri_result_1',
    'final_jinri_result_1':'final_jinri_result_1',
    'jinri_request_1':'jinri_task_request_1',
    'send_jinri_result_1':'send_jinri_result_1',
    'response_jinri_result_1':'response_jinri_result_1',

    'send_jinri_task_2': 'jinri_task_2',
    'response_jinri_task_2': 'Ack_jinri_task_2',
    'take_jinri_result_2': 'take_jinri_result_2',
    'final_jinri_result_2': 'final_jinri_result_2',
    'jinri_request_2': 'jinri_task_request_2',
    'send_jinri_result_2': 'send_jinri_result_2',
    'response_jinri_result_2': 'response_jinri_result_2',

    'send_jinri_task_3': 'jinri_task_3',
    'response_jinri_task_3': 'Ack_jinri_task_3',
    'take_jinri_result_3': 'take_jinri_result_3',
    'final_jinri_result_3': 'final_jinri_result_3',
    'jinri_request_3': 'jinri_task_request_3',
    'send_jinri_result_3': 'send_jinri_result_3',
    'response_jinri_result_3': 'response_jinri_result_3',

    'send_ltp_task': 'ltp_task',
    'response_ltp_task': 'Ack_ltp_task',
    'take_ltp_result': 'take_ltp_result',
    'final_ltp_result': 'final_ltp_result',
    'ltp_request': 'ltp_task_request',
    'send_ltp_result': 'send_ltp_result',
    'response_ltp_result': 'response_ltp_result',

    'send_stan_nlp_task': 'stan_nlp_task',
    'response_stan_nlp_task': 'Ack_stan_nlp_task',
    'take_stan_nlp_result': 'take_stan_nlp_result',
    'final_stan_nlp_result': 'final_stan_nlp_result',
    'stan_nlp_request': 'stan_nlp_task_request',
    'send_stan_nlp_result': 'send_stan_nlp_result',
    'response_stan_nlp_result': 'response_stan_nlp_result',
}

node_type = {
    'simComputing_task':'sim',
     'Search_task':'craw',
    'textparse_task':'textparse',
    'deal_task':'deal',
    'image_task':'image',
    'send_search2_task':'baidu_google_search',
    'send_ltp_task': 'ltp',
    'send_stan_nlp_task': 'stan_nlp',
}

