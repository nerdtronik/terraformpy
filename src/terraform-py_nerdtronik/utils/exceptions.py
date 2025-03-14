class CommandError(Exception):
    def __init__(self, err: str, code: int, stdout: str, stderr: str):
        self.code = code
        self.stdout = stdout
        self.stderr = stderr
        self.err = err
        # Build a detailed error message
        full_message = ""
        full_message += f"\nCode: {code}"
        if len(stdout) > 0:
            full_message += f"\nStdout:\n{stdout}"
        full_message += f"\nStderr:\n{stderr}"
        full_message += f"\nDetails:\n{err}"
        super().__init__(full_message)


class TerraformError(Exception):
    """Base exception class for all Terraform-related errors.

    This class serves as the foundation for all specialized Terraform
    exceptions, providing consistent error handling patterns.

    Attributes:
        message (str): The error message
        command (str): The Terraform command that failed (optional)
        stderr (str): Standard error output from Terraform (optional)
        duration (float): Time taken before the error occurred (optional)
    """

    def __init__(self, message, command=None, stderr=None, duration=None):
        self.message = message
        self.command = command
        self.stderr = stderr
        self.duration = duration

        # Build a detailed error message
        full_message = message
        if command:
            full_message += f"\nCommand: {command}"
        if duration is not None:
            full_message += f"\nDuration: {duration:.4f}s"
        if stderr:
            full_message += f"\nDetails:\n{stderr}"

        super().__init__(full_message)


class TerraformInitError(TerraformError):
    """Exception raised when 'terraform init' fails."""


class TerraformPlanError(TerraformError):
    """Exception raised when 'terraform plan' fails."""


class TerraformApplyError(TerraformError):
    """Exception raised when 'terraform apply' fails."""


class TerraformShowError(TerraformError):
    """Exception raised when 'terraform show' fails."""


class TerraformDestroyError(TerraformError):
    """Exception raised when 'terraform destroy' fails."""


class TerraformOutputError(TerraformError):
    """Exception raised when 'terraform output' fails."""


class TerraformWorkspaceError(TerraformError):
    """Exception raised when workspace operations fail."""


class TerraformValidateError(TerraformError):
    """Exception raised when 'terraform validate' fails."""


class TerraformVersionError(TerraformError):
    """Exception raised when there are issues with the Terraform version."""


class TerraformJsonError(TerraformError):
    """Exception raised when JSON parsing of Terraform output fails."""


class TerraformGetError(TerraformError):
    """Exception raised when 'terraform get' fails."""


class TerraformLoginError(TerraformError):
    """Exception raised when 'terraform login' fails."""


class TerraformLogoutError(TerraformError):
    """Exception raised when 'terraform login' fails."""


class TerraformFmtError(TerraformError):
    """Exception raised when 'terraform fmt' fails."""


class TerraformGraphError(TerraformError):
    """Exception raised when 'terraform graph' fails."""


class TerraformImportError(TerraformError):
    """Exception raised when 'terraform import' fails."""


class TerraformRefreshError(TerraformError):
    """Exception raised when 'terraform refresh' fails."""


class TerraformTaintError(TerraformError):
    """Exception raised when 'terraform taint' fails."""


class TerraformUntaintError(TerraformError):
    """Exception raised when 'terraform untaint' fails."""


class TerraformStateError(TerraformError):
    """Exception raised when 'terraform state' fails."""


class TerraformStateListError(TerraformStateError):
    """Exception raised when 'terraform state list' fails."""


class TerraformStateMvError(TerraformStateError):
    """Exception raised when 'terraform state mv' fails."""


class TerraformStateRmError(TerraformStateError):
    """Exception raised when 'terraform state rm' fails."""


class TerraformStatePullError(TerraformStateError):
    """Exception raised when 'terraform state pull' fails."""


class TerraformStateReplaceProviderError(TerraformStateError):
    """Exception raised when 'terraform state replace-provider' fails."""
