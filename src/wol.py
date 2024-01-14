# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import os
import sys

from typing import List

from alibabacloud_iot20180120.client import Client as Iot20180120Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_iot20180120 import models as iot_20180120_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_console.client import Client as ConsoleClient
from alibabacloud_tea_util.client import Client as UtilClient

from dotenv import load_dotenv

load_dotenv()


class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client(
        access_key_id: str,
        access_key_secret: str,
    ) -> Iot20180120Client:
        """
        使用AK&SK初始化账号Client
        @param access_key_id:
        @param access_key_secret:
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config(
            # 必填，您的 AccessKey ID,
            access_key_id=access_key_id,
            # 必填，您的 AccessKey Secret,
            access_key_secret=access_key_secret
        )
        # Endpoint 请参考 https://api.aliyun.com/product/Iot
        config.endpoint = f'iot.cn-shanghai.aliyuncs.com'
        return Iot20180120Client(config)

    @staticmethod
    def create_client_with_sts(
        access_key_id: str,
        access_key_secret: str,
        security_token: str,
    ) -> Iot20180120Client:
        """
        使用STS鉴权方式初始化账号Client，推荐此方式。
        @param access_key_id:
        @param access_key_secret:
        @param security_token:
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config(
            # 必填，您的 AccessKey ID,
            access_key_id=access_key_id,
            # 必填，您的 AccessKey Secret,
            access_key_secret=access_key_secret,
            # 必填，您的 Security Token,
            security_token=security_token,
            # 必填，表明使用 STS 方式,
            type='sts'
        )
        # Endpoint 请参考 https://api.aliyun.com/product/Iot
        config.endpoint = f'iot.cn-shanghai.aliyuncs.com'
        return Iot20180120Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        # 请确保代码运行环境设置了环境变量 ALIBABA_CLOUD_ACCESS_KEY_ID 和 ALIBABA_CLOUD_ACCESS_KEY_SECRET。
        # 工程代码泄露可能会导致 AccessKey 泄露，并威胁账号下所有资源的安全性。以下代码示例仅供参考，建议使用更安全的 STS 方式，更多鉴权访问方式请参见：https://help.aliyun.com/document_detail/378659.html
        client = Sample.create_client(os.environ['ALIBABA_CLOUD_ACCESS_KEY_ID'], os.environ['ALIBABA_CLOUD_ACCESS_KEY_SECRET'])

        # 检查命令行参数以确定控制哪台电脑
        if not args or args[0] not in ['1', '2', '3', '4']:
            raise ValueError("请提供有效的电脑ID（1, 2, 3, 4）作为命令行参数。")

        # 设置items参数以控制对应的电脑
        computer_id = args[0]
        items = '{"SocketSwitch_' + computer_id + '":1}'

        set_device_property_request = iot_20180120_models.SetDevicePropertyRequest(
            product_key='hcixs0UnFim',
            device_name='WOL-tool',
            items=items,
            iot_instance_id='iot-06z00fbux1czr44'
        )
        runtime = util_models.RuntimeOptions()
        try:
            resp = client.set_device_property_with_options(set_device_property_request, runtime)
            ConsoleClient.log(UtilClient.to_jsonstring(resp))
        except Exception as error:
            # 错误 message
            print(error.message)
            # 诊断地址
            print(error.data.get("Recommend"))
            UtilClient.assert_as_string(error.message)

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        # 请确保代码运行环境设置了环境变量 ALIBABA_CLOUD_ACCESS_KEY_ID 和 ALIBABA_CLOUD_ACCESS_KEY_SECRET。
        # 工程代码泄露可能会导致 AccessKey 泄露，并威胁账号下所有资源的安全性。以下代码示例仅供参考，建议使用更安全的 STS 方式，更多鉴权访问方式请参见：https://help.aliyun.com/document_detail/378659.html
        client = Sample.create_client(os.environ['ALIBABA_CLOUD_ACCESS_KEY_ID'], os.environ['ALIBABA_CLOUD_ACCESS_KEY_SECRET'])

        # 检查命令行参数以确定控制哪台电脑
        if not args or args[0] not in ['1', '2', '3', '4']:
            raise ValueError("请提供有效的电脑ID（1, 2, 3, 4）作为命令行参数。")
        
        # 设置items参数以控制对应的电脑
        computer_id = args[0]
        items = '{"SocketSwitch_' + computer_id + '":1}'

        set_device_property_request = iot_20180120_models.SetDevicePropertyRequest(
            product_key='hcixs0UnFim',
            device_name='WOL-tool',
            items=items,
            iot_instance_id='iot-06z00fbux1czr44'
        )
        runtime = util_models.RuntimeOptions()
        try:
            resp = await client.set_device_property_with_options_async(set_device_property_request, runtime)
            ConsoleClient.log(UtilClient.to_jsonstring(resp))
        except Exception as error:
            # 错误 message
            print(error.message)
            # 诊断地址
            print(error.data.get("Recommend"))
            UtilClient.assert_as_string(error.message)


if __name__ == '__main__':
    Sample.main(sys.argv[1:])
