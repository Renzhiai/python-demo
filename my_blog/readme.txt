1.cd f:/pythonwork      ���л�����Ӧ��Ŀ¼��
2.django-admin startproject my_blog     ����һ����Ŀ
3.cd my_blog    �л�����Ӧ����Ŀ��
4.python manage.py startapp article     ����һ��app
    article��һ��app��һ��app����һ������ģ��
5.��my_blog/my_blog/settings.py������½�app��article
6.python manage.py runserver localhost:9000     ����

һ��Models
    1.Django Model
        a��ÿһ��Django Model���̳���django.db.models.Model
        b����Model����ÿһ������attribute������һ��database field
        c��ͨ��Django Model API����ִ�����ݿ����ɾ�Ĳ�, ������ҪдһЩ���ݿ�Ĳ�ѯ���
    2.�������ݿ�
        my_blog/my_blog/settings.py�п��Բ鿴���޸����ݿ�����
    3.����models
        ��my_blog/article/models.py�±�д����
        a��CharField ���ڴ洢�ַ���, max_length������󳤶�
        b��TextField ���ڴ洢�����ı�
        c��DateTimeField ���ڴ洢ʱ��, auto_now_add����True��ʾ�Զ����ö�������ʱ��
    4.ͬ�����ݿ�
        python manage.py makemigrations
        python manage.py migrate

����Admin
    1.����url
        ��my_blog/my_blog/urls.py������ url(r'^admin/', admin.site.urls)
    2.���������û�
        python manage.py createsuperuser
        �˺�:admin
        ����:admin123

����Views��URL
    1.��ҳ������߼�
    request����->�ӷ�������ȡ����->��������->����ҳ���ֳ���
        url�����൱�ڿͻ��������������request��������, ������ָ��Ҫ���õĳ����߼�
        views������������߼�, Ȼ����ֵ�template(һ��ΪGET����, POST�������в�ͬ)
        templateһ��Ϊhtml+CSS����ʽ, ��Ҫ�ǳ��ָ��û��ı�����ʽ

    2.url()�������ĸ�����, �����Ǳ����:regex��view, ������ѡ��:kwargs��name
        regex��regular expression�ļ�д,�����ַ����е�ģʽƥ���һ���﷨, Django �������URL������������ƥ���б��е�������ʽ��ֱ��ƥ�䵽һ��Ϊֹ��
        view��Djangoƥ����һ��������ʽ�ͻ����ָ����view�߼�, ��������л����article/views.py�е�home����
        kwargs����ؼ��ֲ����ɴ�һ���ֵ���Ŀ��view
        name������� URL, ʹurl�� Django �������ط�ʹ��, �ر�����ģ����