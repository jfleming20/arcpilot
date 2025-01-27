from uuid import uuid4

from claims.domain.repositories import claim_repository

from outbox.domain.command.create_published import CreatePublishedCommand
from outbox.domain.app import app


class CloseClaimCommand:
    def __init__(self):
        self.uuid = str(uuid4())
def close_claim_command_handler(command: CloseClaimCommand) -> str:
    claim = claim_repository.get(command.claim_uuid)
    # claim.closed = True
    claim_repository.update(claim)

    claim_closed_successfully_command = CreatePublishedCommand(
        destination="/topic/claim",
        body={"claim_uuid": claim.uuid}
    )

    claim_closure_failed_command = CreatePublishedCommand(
        destination="/topic/claim",
        body={"claim_uuid": claim.uuid}
    )

    app.execute_command(claim_closed_successfully_command)

    app.execute_command(claim_closure_failed_command)

    return claim.uuid
