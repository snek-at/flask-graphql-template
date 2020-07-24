import graphene
from flask_graphql_auth import get_jwt_identity, mutation_jwt_required

from app.model import PostModel, AccountModel
from app.model.post import CommentModel
from app.schema.unions.mutation import ResponseUnion
from app.schema.fields import ResponseMessageField


class CommentLeaveMutation(graphene.Mutation):
    class Arguments(object):
        token = graphene.String()
        post_id = graphene.Int()
        comment = graphene.String()

    result = graphene.Field(ResponseUnion)

    @classmethod
    @mutation_jwt_required
    def mutate(cls, _, info, post_id, comment):
        post = PostModel.objects(id=post_id).first()
        new_comment = CommentModel(
            text=comment, author=AccountModel.objects(id=get_jwt_identity()).first()
        )

        if post is None:
            return CommentLeaveMutation(
                ResponseMessageField(is_success=False, message="Unknown post id")
            )

        post.update_one(push_comment=new_comment)

        return CommentLeaveMutation(
            ResponseMessageField(
                is_success=True, message="Comment successfully uploaded"
            )
        )

