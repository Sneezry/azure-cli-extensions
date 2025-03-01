# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "stack-hci extension create",
)
class Create(AAZCommand):
    """Create extension for HCI cluster.

    :example: Create arc extension
        az stack-hci extension create --arc-setting-name "default" --cluster-name "myCluster" --type "MicrosoftMonitoringAgent" --protected-settings "{workspaceKey:xx}" --publisher "Microsoft.Compute" --settings "{workspaceId:xx}" --type-handler-version "1.10" --name "MicrosoftMonitoringAgent" --resource-group "test-rg"
    """

    _aaz_info = {
        "version": "2023-03-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.azurestackhci/clusters/{}/arcsettings/{}/extensions/{}", "2023-03-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.arc_setting_name = AAZStrArg(
            options=["--arc-setting-name"],
            help="The name of the proxy resource holding details of HCI ArcSetting information.",
            required=True,
        )
        _args_schema.cluster_name = AAZStrArg(
            options=["--cluster-name"],
            help="The name of the cluster.",
            required=True,
        )
        _args_schema.extension_name = AAZStrArg(
            options=["-n", "--name", "--extension-name"],
            help="The name of the machine extension.",
            required=True,
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "ExtensionParameters"

        _args_schema = cls._args_schema
        _args_schema.auto_upgrade = AAZBoolArg(
            options=["--auto-upgrade"],
            arg_group="ExtensionParameters",
            help="Indicates whether the extension should use a newer minor version if one is available at deployment time. Once deployed, however, the extension will not upgrade minor versions unless redeployed, even with this property set to true.",
        )
        _args_schema.force_update_tag = AAZStrArg(
            options=["--force-update-tag"],
            arg_group="ExtensionParameters",
            help="How the extension handler should be forced to update even if the extension configuration has not changed.",
        )
        _args_schema.protected_settings = AAZObjectArg(
            options=["--protected-settings"],
            arg_group="ExtensionParameters",
            help="Protected settings (may contain secrets).",
        )
        _args_schema.publisher = AAZStrArg(
            options=["--publisher"],
            arg_group="ExtensionParameters",
            help="The name of the extension handler publisher.",
        )
        _args_schema.settings = AAZObjectArg(
            options=["--settings"],
            arg_group="ExtensionParameters",
            help="Json formatted public settings for the extension.",
        )
        _args_schema.type = AAZStrArg(
            options=["--type"],
            arg_group="ExtensionParameters",
            help="Specifies the type of the extension; an example is \"CustomScriptExtension\".",
        )
        _args_schema.type_handler_version = AAZStrArg(
            options=["--type-handler-version"],
            arg_group="ExtensionParameters",
            help="Specifies the version of the script handler. Latest version would be used if not specified.",
        )

        protected_settings = cls._args_schema.protected_settings
        protected_settings.workspace_key = AAZStrArg(
            options=["workspace-key"],
            help="Workspace Key.",
        )

        settings = cls._args_schema.settings
        settings.workspace_id = AAZStrArg(
            options=["workspace-id"],
            help="Workspace Id.",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.ExtensionsCreate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class ExtensionsCreate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AzureStackHCI/clusters/{clusterName}/arcSettings/{arcSettingName}/extensions/{extensionName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "arcSettingName", self.ctx.args.arc_setting_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "clusterName", self.ctx.args.cluster_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "extensionName", self.ctx.args.extension_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-03-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("extensionParameters", AAZObjectType)

            extension_parameters = _builder.get(".properties.extensionParameters")
            if extension_parameters is not None:
                extension_parameters.set_prop("autoUpgradeMinorVersion", AAZBoolType, ".auto_upgrade")
                extension_parameters.set_prop("forceUpdateTag", AAZStrType, ".force_update_tag")
                extension_parameters.set_prop("protectedSettings", AAZObjectType, ".protected_settings")
                extension_parameters.set_prop("publisher", AAZStrType, ".publisher")
                extension_parameters.set_prop("settings", AAZObjectType, ".settings")
                extension_parameters.set_prop("type", AAZStrType, ".type")
                extension_parameters.set_prop("typeHandlerVersion", AAZStrType, ".type_handler_version")

            protected_settings = _builder.get(".properties.extensionParameters.protectedSettings")
            if protected_settings is not None:
                protected_settings.set_prop("workspaceKey", AAZStrType, ".workspace_key")

            settings = _builder.get(".properties.extensionParameters.settings")
            if settings is not None:
                settings.set_prop("workspaceId", AAZStrType, ".workspace_id")

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()

            _schema_on_200_201 = cls._schema_on_200_201
            _schema_on_200_201.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200_201.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200_201.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200_201.properties
            properties.aggregate_state = AAZStrType(
                serialized_name="aggregateState",
                flags={"read_only": True},
            )
            properties.extension_parameters = AAZObjectType(
                serialized_name="extensionParameters",
            )
            properties.managed_by = AAZStrType(
                serialized_name="managedBy",
                flags={"read_only": True},
            )
            properties.per_node_extension_details = AAZListType(
                serialized_name="perNodeExtensionDetails",
                flags={"read_only": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )

            extension_parameters = cls._schema_on_200_201.properties.extension_parameters
            extension_parameters.auto_upgrade_minor_version = AAZBoolType(
                serialized_name="autoUpgradeMinorVersion",
            )
            extension_parameters.enable_automatic_upgrade = AAZBoolType(
                serialized_name="enableAutomaticUpgrade",
            )
            extension_parameters.force_update_tag = AAZStrType(
                serialized_name="forceUpdateTag",
            )
            extension_parameters.protected_settings = AAZObjectType(
                serialized_name="protectedSettings",
            )
            extension_parameters.publisher = AAZStrType()
            extension_parameters.settings = AAZObjectType()
            extension_parameters.type = AAZStrType()
            extension_parameters.type_handler_version = AAZStrType(
                serialized_name="typeHandlerVersion",
            )

            protected_settings = cls._schema_on_200_201.properties.extension_parameters.protected_settings
            protected_settings.workspace_key = AAZStrType(
                serialized_name="workspaceKey",
            )

            settings = cls._schema_on_200_201.properties.extension_parameters.settings
            settings.workspace_id = AAZStrType(
                serialized_name="workspaceId",
            )

            per_node_extension_details = cls._schema_on_200_201.properties.per_node_extension_details
            per_node_extension_details.Element = AAZObjectType()

            _element = cls._schema_on_200_201.properties.per_node_extension_details.Element
            _element.extension = AAZStrType(
                flags={"read_only": True},
            )
            _element.instance_view = AAZObjectType(
                serialized_name="instanceView",
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.state = AAZStrType(
                flags={"read_only": True},
            )
            _element.type_handler_version = AAZStrType(
                serialized_name="typeHandlerVersion",
                flags={"read_only": True},
            )

            instance_view = cls._schema_on_200_201.properties.per_node_extension_details.Element.instance_view
            instance_view.name = AAZStrType()
            instance_view.status = AAZObjectType()
            instance_view.type = AAZStrType()
            instance_view.type_handler_version = AAZStrType(
                serialized_name="typeHandlerVersion",
            )

            status = cls._schema_on_200_201.properties.per_node_extension_details.Element.instance_view.status
            status.code = AAZStrType()
            status.display_status = AAZStrType(
                serialized_name="displayStatus",
            )
            status.level = AAZStrType()
            status.message = AAZStrType()
            status.time = AAZStrType()

            system_data = cls._schema_on_200_201.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            return cls._schema_on_200_201


class _CreateHelper:
    """Helper class for Create"""


__all__ = ["Create"]
