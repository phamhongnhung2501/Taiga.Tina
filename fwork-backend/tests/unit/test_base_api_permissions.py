# -*- coding: utf-8 -*-

from tina.base.api.permissions import (AllowAny as TruePermissionComponent,
                                       DenyAll as FalsePermissionComponent)


def test_permission_component_composition():
    assert (TruePermissionComponent() | TruePermissionComponent()).check_permissions(None, None, None)
    assert (TruePermissionComponent() | FalsePermissionComponent()).check_permissions(None, None, None)
    assert (FalsePermissionComponent() | TruePermissionComponent()).check_permissions(None, None, None)
    assert not (FalsePermissionComponent() | FalsePermissionComponent()).check_permissions(None, None, None)

    assert (TruePermissionComponent() & TruePermissionComponent()).check_permissions(None, None, None)
    assert not (TruePermissionComponent() & FalsePermissionComponent()).check_permissions(None, None, None)
    assert not (FalsePermissionComponent() & TruePermissionComponent()).check_permissions(None, None, None)
    assert not (FalsePermissionComponent() & FalsePermissionComponent()).check_permissions(None, None, None)

    assert (~FalsePermissionComponent()).check_permissions(None, None, None)
    assert not (~TruePermissionComponent()).check_permissions(None, None, None)
