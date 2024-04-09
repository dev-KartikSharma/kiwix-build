from .base import ConfigInfo


class NeutralConfigInfo(ConfigInfo):
    name = "neutral"
    arch_name = "neutral"
    static = ""
    compatible_hosts = ["fedora", "debian", "Darwin"]

    def __str__(self):
        return "neutral"
