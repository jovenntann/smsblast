# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Ussd(models.Model):
    termid = models.CharField(db_column='TERMID', max_length=64)  # Field name made lowercase.
    ussd_msg = models.CharField(db_column='USSD_MSG', max_length=255)  # Field name made lowercase.
    ussd_return = models.CharField(db_column='USSD_RETURN', max_length=255)  # Field name made lowercase.
    error_msg = models.CharField(db_column='ERROR_MSG', max_length=64)  # Field name made lowercase.
    inserttime = models.DateTimeField(db_column='INSERTTIME')  # Field name made lowercase.
    type = models.IntegerField()
    card = models.CharField(max_length=64)
    recharge_ok = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'USSD'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Auto(models.Model):
    auto_reply = models.IntegerField(blank=True, null=True)
    reply_num_except = models.TextField()
    reply_msg = models.TextField()
    auto_send = models.IntegerField(blank=True, null=True)
    auto_send_num = models.CharField(max_length=64)
    auto_send_msg = models.TextField()
    auto_send_timeout = models.IntegerField()
    all_send_num = models.CharField(max_length=64)
    all_send_msg = models.TextField()

    class Meta:
        managed = False
        db_table = 'auto'


class AutoUssd(models.Model):
    name = models.CharField(max_length=32)
    type = models.IntegerField()
    auto_sms_num = models.CharField(max_length=32)
    auto_sms_msg = models.CharField(max_length=320)
    auto_ussd = models.CharField(max_length=160)
    prov_id = models.IntegerField()
    goip_id = models.IntegerField()
    crontime = models.IntegerField()
    bal_sms_r = models.CharField(max_length=160)
    bal_ussd_r = models.CharField(max_length=160)
    bal_limit = models.FloatField()
    recharge_ussd = models.CharField(max_length=160)
    last_time = models.DateTimeField()
    next_time = models.IntegerField()
    send_sms = models.CharField(max_length=128)
    send_email = models.CharField(max_length=32)
    recharge_type = models.IntegerField()
    recharge_ussd1 = models.CharField(max_length=160)
    recharge_ussd1_goip = models.IntegerField()
    recharge_ok_r = models.CharField(max_length=64)
    recharge_ok_r2 = models.CharField(max_length=64)
    bal_ussd_zero_match_char = models.CharField(max_length=160)
    bal_sms_zero_match_char = models.CharField(max_length=160)
    disable_if_low_bal = models.IntegerField()
    group_id = models.IntegerField()
    auto_disconnect_after_bal = models.IntegerField()
    disable_callout_when_bal = models.IntegerField()
    ussd2 = models.CharField(max_length=160)
    ussd2_ok_match = models.CharField(max_length=160)
    ussd22 = models.CharField(max_length=160)
    ussd22_ok_match = models.CharField(max_length=160)
    send_mail2 = models.CharField(max_length=32)
    disable_if_ussd2_undone = models.IntegerField()
    recharge_limit = models.IntegerField()
    send_sms2 = models.CharField(max_length=32)
    recharge_sms_num = models.CharField(max_length=32)
    recharge_sms_msg = models.CharField(max_length=160)
    recharge_sms_ok_num = models.CharField(max_length=32)
    auto_ussd_step2 = models.CharField(max_length=160)
    auto_ussd_step2_start_r = models.CharField(max_length=160)
    sms_report_goip = models.IntegerField()
    bal_delay = models.IntegerField()
    re_step2_enable = models.IntegerField()
    re_step2_cmd = models.CharField(max_length=64)
    re_step2_ok_r = models.CharField(max_length=64)
    auto_reset_remain_enable = models.IntegerField()
    auto_ussd_step3 = models.CharField(max_length=160)
    auto_ussd_step3_start_r = models.CharField(max_length=160)
    auto_ussd_step4 = models.CharField(max_length=160)
    auto_ussd_step4_start_r = models.CharField(max_length=160)
    recharge_con_type = models.IntegerField()
    fixed_time = models.CharField(max_length=10)
    remain_limit = models.IntegerField()
    remain_set = models.IntegerField()
    fixed_next_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auto_ussd'


class Crowd(models.Model):
    name = models.CharField(max_length=20)
    info = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crowd'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMailboxMailbox(models.Model):
    name = models.CharField(max_length=255)
    uri = models.CharField(max_length=255, blank=True, null=True)
    from_email = models.CharField(max_length=255, blank=True, null=True)
    active = models.IntegerField()
    last_polling = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_mailbox_mailbox'


class DjangoMailboxMessage(models.Model):
    subject = models.CharField(max_length=255)
    message_id = models.CharField(max_length=255)
    from_header = models.CharField(max_length=255)
    to_header = models.TextField()
    outgoing = models.IntegerField()
    body = models.TextField()
    encoded = models.IntegerField()
    processed = models.DateTimeField()
    read = models.DateTimeField(blank=True, null=True)
    in_reply_to = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    mailbox = models.ForeignKey(DjangoMailboxMailbox, models.DO_NOTHING)
    eml = models.CharField(max_length=100, blank=True, null=True)
    flag = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_mailbox_message'


class DjangoMailboxMessageattachment(models.Model):
    headers = models.TextField(blank=True, null=True)
    document = models.CharField(max_length=100)
    message = models.ForeignKey(DjangoMailboxMessage, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_mailbox_messageattachment'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Goip(models.Model):
    name = models.CharField(unique=True, max_length=64)
    provider = models.IntegerField()
    host = models.CharField(max_length=50)
    port = models.IntegerField()
    password = models.CharField(max_length=64)
    alive = models.IntegerField()
    num = models.CharField(max_length=30)
    signal = models.IntegerField(blank=True, null=True)
    gsm_status = models.CharField(max_length=30)
    voip_status = models.CharField(max_length=30)
    voip_state = models.CharField(max_length=30)
    bal = models.FloatField(blank=True, null=True)
    cellinfo = models.CharField(db_column='CELLINFO', max_length=160)  # Field name made lowercase.
    cgatt = models.CharField(db_column='CGATT', max_length=32)  # Field name made lowercase.
    bcch = models.CharField(db_column='BCCH', max_length=160)  # Field name made lowercase.
    bal_time = models.DateTimeField(blank=True, null=True)
    keepalive_time = models.DateTimeField(blank=True, null=True)
    gsm_login_time = models.DateTimeField(blank=True, null=True)
    gsm_login_time_t = models.IntegerField()
    keepalive_time_t = models.IntegerField()
    remain_time = models.IntegerField()
    imei = models.CharField(max_length=15, blank=True, null=True)
    imsi = models.CharField(max_length=32, blank=True, null=True)
    iccid = models.CharField(max_length=32, blank=True, null=True)
    last_call_record_id = models.IntegerField()
    remain_count = models.IntegerField()
    count_limit = models.IntegerField()
    remain_count_d = models.IntegerField()
    count_limit_d = models.IntegerField()
    group_id = models.IntegerField()
    report_mail = models.CharField(max_length=64)
    fwd_mail_enable = models.IntegerField()
    report_http = models.CharField(max_length=64)
    fwd_http_enable = models.IntegerField()
    carrier = models.CharField(max_length=32)
    auto_num_c = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'goip'


class GoipGroup(models.Model):
    group_name = models.CharField(unique=True, max_length=32)

    class Meta:
        managed = False
        db_table = 'goip_group'


class Groups(models.Model):
    name = models.CharField(max_length=20)
    info = models.CharField(max_length=100, blank=True, null=True)
    crowdid = models.ForeignKey(Crowd, models.DO_NOTHING, db_column='crowdid')

    class Meta:
        managed = False
        db_table = 'groups'


class ImeiDb(models.Model):
    imei = models.CharField(max_length=15)
    goipid = models.IntegerField()
    goipname = models.CharField(max_length=64)
    used = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'imei_db'


class Message(models.Model):
    crontime = models.IntegerField()
    time = models.DateTimeField()
    userid = models.IntegerField()
    cronid = models.IntegerField()
    msg = models.TextField()
    type = models.IntegerField()
    receiverid = models.TextField(blank=True, null=True)
    receiverid1 = models.TextField(blank=True, null=True)
    receiverid2 = models.TextField(blank=True, null=True)
    groupid = models.TextField(blank=True, null=True)
    groupid1 = models.TextField(blank=True, null=True)
    groupid2 = models.TextField(blank=True, null=True)
    recv = models.IntegerField()
    recv1 = models.IntegerField()
    recv2 = models.IntegerField()
    over = models.IntegerField()
    stoptime = models.IntegerField(blank=True, null=True)
    tel = models.TextField(blank=True, null=True)
    prov = models.CharField(max_length=30, blank=True, null=True)
    goipid = models.IntegerField(blank=True, null=True)
    uid = models.CharField(max_length=64, blank=True, null=True)
    msgid = models.IntegerField(blank=True, null=True)
    total = models.IntegerField()
    card_id = models.IntegerField()
    card = models.CharField(max_length=64)
    resend = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'message'


class Prov(models.Model):
    prov = models.CharField(max_length=30, blank=True, null=True)
    inter = models.CharField(max_length=10, blank=True, null=True)
    local = models.CharField(max_length=10, blank=True, null=True)
    recharge_ok_r = models.CharField(max_length=64)
    auto_num_ussd = models.CharField(max_length=20)
    num_prefix = models.CharField(max_length=20)
    num_postfix = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'prov'


class Receive(models.Model):
    srcnum = models.CharField(max_length=30)
    provid = models.IntegerField()
    msg = models.TextField()
    time = models.DateTimeField()
    goipid = models.IntegerField()
    goipname = models.CharField(max_length=30)
    srcid = models.IntegerField()
    srcname = models.CharField(max_length=30)
    srclevel = models.IntegerField()
    status = models.IntegerField()
    smscnum = models.CharField(max_length=32)
    flag = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'receive'


class Receiver(models.Model):
    no = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    name_l = models.CharField(max_length=20)
    ename_f = models.CharField(max_length=30)
    ename_l = models.CharField(max_length=30)
    gender = models.CharField(max_length=1)
    info = models.CharField(max_length=100)
    tel = models.CharField(max_length=20, blank=True, null=True)
    hometel = models.CharField(max_length=20)
    officetel = models.CharField(max_length=20)
    provider = models.CharField(max_length=20)
    dead = models.IntegerField()
    reject = models.IntegerField()
    name1 = models.CharField(max_length=20)
    tel1 = models.CharField(max_length=20, blank=True, null=True)
    provider1 = models.CharField(max_length=20)
    name2 = models.CharField(max_length=20)
    tel2 = models.CharField(max_length=20, blank=True, null=True)
    provider2 = models.CharField(max_length=20)
    upload_time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'receiver'


class RechargeCard(models.Model):
    card = models.CharField(max_length=64)
    prov_id = models.IntegerField()
    used = models.IntegerField()
    use_time = models.DateTimeField(blank=True, null=True)
    goipid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recharge_card'


class Record(models.Model):
    goipid = models.IntegerField()
    dir = models.IntegerField()
    num = models.CharField(max_length=64)
    time = models.DateTimeField()
    expiry = models.IntegerField(blank=True, null=True)
    hangup_cause = models.CharField(db_column='HANGUP_CAUSE', max_length=32)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'record'


class Recvgroup(models.Model):
    groupsid = models.ForeignKey(Groups, models.DO_NOTHING, db_column='groupsid')
    recvid = models.ForeignKey(Receiver, models.DO_NOTHING, db_column='recvid')

    class Meta:
        managed = False
        db_table = 'recvgroup'


class Refcrowd(models.Model):
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userid')
    crowdid = models.ForeignKey(Crowd, models.DO_NOTHING, db_column='crowdid')

    class Meta:
        managed = False
        db_table = 'refcrowd'


class Refgroup(models.Model):
    groupsid = models.ForeignKey(Groups, models.DO_NOTHING, db_column='groupsid')
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userid')

    class Meta:
        managed = False
        db_table = 'refgroup'


class Sends(models.Model):
    time = models.DateTimeField()
    userid = models.IntegerField()
    messageid = models.ForeignKey(Message, models.DO_NOTHING, db_column='messageid')
    goipid = models.IntegerField()
    provider = models.CharField(max_length=20)
    telnum = models.CharField(max_length=20)
    recvlev = models.IntegerField()
    recvid = models.IntegerField()
    over = models.IntegerField(blank=True, null=True)
    error_no = models.IntegerField(blank=True, null=True)
    msg = models.TextField()
    received = models.IntegerField()
    sms_no = models.IntegerField()
    total = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sends'


class SirvasmsappContact(models.Model):
    date = models.DateTimeField()
    name = models.CharField(max_length=80)
    number = models.CharField(max_length=20)
    group = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'sirvasmsapp_contact'


class SirvasmsappDaterange(models.Model):
    date_from = models.DateField()
    date_to = models.DateField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sirvasmsapp_daterange'


class SirvasmsappQueue(models.Model):
    date = models.DateTimeField()
    from_number = models.CharField(max_length=20)
    to_number = models.CharField(max_length=20)
    user = models.CharField(max_length=80)
    message = models.CharField(max_length=1000)
    flag = models.IntegerField()
    tag = models.CharField(max_length=80)
    goip = models.CharField(max_length=80)
    datesent = models.DateTimeField(db_column='dateSent')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sirvasmsapp_queue'


class SirvasmsappQueueblast(models.Model):
    date = models.DateTimeField()
    tag = models.CharField(max_length=80)
    message = models.CharField(max_length=1000)
    status = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'sirvasmsapp_queueblast'


class SirvasmsappRate(models.Model):
    code = models.CharField(max_length=10)
    abbreviation = models.CharField(max_length=4)
    country = models.CharField(max_length=50)
    buy = models.DecimalField(max_digits=8, decimal_places=6)
    sell = models.DecimalField(max_digits=8, decimal_places=6)
    route = models.CharField(max_length=20)
    source = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'sirvasmsapp_rate'


class SirvasmsappReceived(models.Model):
    date = models.DateTimeField()
    from_number = models.CharField(max_length=80)
    to_number = models.CharField(max_length=80)
    messagesid = models.CharField(db_column='MessageSid', max_length=80)  # Field name made lowercase.
    status = models.CharField(max_length=80)
    message = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'sirvasmsapp_received'


class System(models.Model):
    maxword = models.IntegerField()
    sysname = models.CharField(max_length=20)
    lan = models.IntegerField()
    version = models.IntegerField()
    smtp_user = models.CharField(max_length=64)
    smtp_pass = models.CharField(max_length=64)
    smtp_mail = models.CharField(max_length=64)
    smtp_server = models.CharField(max_length=64)
    smtp_port = models.IntegerField()
    email_report_gsm_logout_enable = models.IntegerField()
    email_report_gsm_logout_time_limit = models.IntegerField()
    email_report_reg_logout_enable = models.IntegerField()
    email_report_reg_logout_time_limit = models.IntegerField()
    report_mail = models.CharField(max_length=64)
    email_report_remain_timeout_enable = models.IntegerField()
    send_page_jump_enable = models.IntegerField()
    endless_send_enable = models.IntegerField()
    re_ask_timer = models.IntegerField()
    total = models.IntegerField()
    this_day = models.IntegerField()
    email_forward_sms_enable = models.IntegerField()
    email_remain_count_enable = models.IntegerField()
    email_remain_count_d_enable = models.IntegerField()
    session_time = models.IntegerField()
    disable_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'system'


class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    permissions = models.IntegerField()
    info = models.TextField(blank=True, null=True)
    msg1 = models.CharField(max_length=320)
    msg2 = models.CharField(max_length=320)
    msg3 = models.CharField(max_length=320)
    msg4 = models.CharField(max_length=320)
    msg5 = models.CharField(max_length=320)
    msg6 = models.CharField(max_length=320)
    msg7 = models.CharField(max_length=320)
    msg8 = models.CharField(max_length=320)
    msg9 = models.CharField(max_length=320)
    msg10 = models.CharField(max_length=320)

    class Meta:
        managed = False
        db_table = 'user'
