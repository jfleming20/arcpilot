from uuid import uuid4

from claims.domain.repositories import claim_repository

from outbox.domain.command.create_published import CreatePublishedCommand
from outbox.domain.app import app


class AssignClaimToAdjusterCommand:
    def __init__(self):
        self.uuid = str(uuid4())
def assign_claim_to_adjuster_command_handler(command: AssignClaimToAdjusterCommand) -> str:
    claim = claim_repository.get(command.claim_uuid)
    # claim.closed = True
    claim_repository.update(claim)

    claim_assigned_to_adjuster_command = CreatePublishedCommand(
        destination="/topic/claim",
        body={"claim_uuid": claim.uuid}
    )

    claim_assignment_failed_command = CreatePublishedCommand(
        destination="/topic/claim",
        body={"claim_uuid": claim.uuid}
    )

    app.execute_command(claim_assigned_to_adjuster_command)

    app.execute_command(claim_assignment_failed_command)

    return claim.uuid
