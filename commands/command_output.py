from commands.status import Status

class CommandOutput:
    def success(cmd):
        output = {}
        output["result"] = None
        output["status"] = Status.SUCCESS.value
        if cmd == "create":
            output["message"] = "Succefully created database"

        return output

    def failure(status):
        output = {}
        output["result"] = None
        for fail_status in Status:
            if status == fail_status:
                output["status"] = fail_status.value
                output["message"] = fail_status.name
                break
        return output
