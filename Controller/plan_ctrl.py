import hashlib

from sqlalchemy import select
#from Utils import session
from Model.models import Plan, convert_json


def get_plans():
    result = init_plans()
    #result = session.execute(select(Plan))
    return result

def init_plans():
    plan_basic = Plan(id_plan=1, name="basico", limit_files=20, limit_data=104857600)
    plan_advanced = Plan(id_plan=2, name="avançado", limit_files=100, limit_data=10485760000)
    plan_unlimited = Plan(id_plan=3, name="ilimitado", limit_files=0, limit_data=0)
    plan_basic = convert_json(id_plan=plan_basic.id_plan, name=plan_basic.name,
                              limit_files=plan_basic.limit_files, limit_data=plan_basic.limit_data)
    plan_advanced = convert_json(id_plan=plan_advanced.id_plan, name=plan_advanced.name,
                              limit_files=plan_advanced.limit_files, limit_data=plan_advanced.limit_data)
    plan_unlimited = convert_json(id_plan=plan_unlimited.id_plan, name=plan_unlimited.name,
                              limit_files=plan_unlimited.limit_files, limit_data=plan_unlimited.limit_data)

    plans_data = [plan_basic, plan_advanced, plan_unlimited]
    #session.add(plan_basic)
    #session.add(plan_advanced)
    #session.add(plan_unlimited)
    #session.commit()
    return list(plans_data)
