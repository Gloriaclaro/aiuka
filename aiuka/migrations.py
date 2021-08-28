from create_teble import ct_reabilitacao, ct_reabilitacao_sp, ct_reabilitacao_tp, ct_necropsia, ct_users, mysql_trigger_id

ct_reabilitacao.create_table()
ct_reabilitacao_sp.create_table()
ct_reabilitacao_tp.create_table()
ct_users.create_table()
ct_necropsia.create_table()
mysql_trigger_id.trigger_reabilitacao()
mysql_trigger_id.trigger_reabilitacao_sp()
mysql_trigger_id.trigger_reabilitacao_tp()
mysql_trigger_id.trigger_necropsia()