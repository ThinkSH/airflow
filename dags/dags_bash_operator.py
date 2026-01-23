from __future__ import annotations

import pendulum
import datetime

from airflow.providers.standard.operators.bash import BashOperator
from airflow.sdk import DAG, chain

with DAG(
    dag_id="dags_bash_operator", #파일면과 dag_id는 맞춰주는게 좋다. 
    schedule=None, #분, 시, 일, 월, 요일
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"), #dag 언제부터 돌꺼냐 
    catchup=False, #start_date 부터 현재까지 누락된 구간 다 돌릴 것이냐 (차례로 도는게 아니고 한꺼번에 돈다.)
    #dagrun_timeout=datetime.timedelta(minutes=60), #60분 이상 돌면 실패
    tags=["example", "example2", "example3"], #태그만 추려서 볼 수 있음
    #params={"example_key": "example_value"}, #dag 밑에 태스크에 공통적으로 넘겨줄 파라미터 
) as dag:
    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command="echo whoami",
    )
    
    bash_t2 = BashOperator(
        task_id="bash_t2",
        bash_command="echo $HOSTNAME",
    )

    bash_t1 >> bash_t2