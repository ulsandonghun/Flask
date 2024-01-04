class User:
    def __init__(self, id, username):
        self.id = id
        self.username = username

    @staticmethod
    def query_all():
        # 실제로는 여기에서 데이터베이스에서 사용자 정보를 조회할 것입니다.
        # 이 예제에서는 간단히 몇 개의 더미 사용자를 반환합니다.
        return [User(1, 'john_doe'), User(2, 'jane_smith')]