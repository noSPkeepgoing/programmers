# [PCCE 모의고사 2] 9번
# 문제 설명
# A회사의 사원들에게는 01100103와 같은 일련번호가 주어집니다. 일련번호는 8자리이며 순서대로 두 자리씩 성별, 소속 부서, 소속 팀, 유효성 번호로 구성되어 있습니다.

# 각 정보는 다음과 같습니다.

# 성별
# male : 01
# female : 02
# 소속 부서
# operation : 10
# sales : 11
# develop : 12
# finance : 13
# law : 14
# research : 15
# 소속 팀
# Nteam : N
# 유효성 번호
# valid: 유효성 번호를 제외한 6개의 숫자들을 모두 더해 13으로 나눈 나머지가 유효성 번호와 같을 때
# invalid: 유효성 번호를 제외한 6개의 숫자들을 모두 더해 13으로 나눈 나머지가 유효성 번호와 다를 때
# 일련번호를 해석하는 방법은 다음과 같습니다.

# 1 단계. 일련번호를 앞에서부터 두 자리씩 끊어 저장합니다.
# 2 단계. 각 자리별로 위의 정보와 비교하여 문자열로 변경합니다.
# 예를 들어 일련번호가 01100103이면 male, operation, 1team이고 유효성 번호가 나머지 6개의 숫자를 모두 더한 (0 + 1 + 1 + 0 + 0 + 1 = 3)을 13으로 나눈 나머지 (3 % 13 = 3)과 같기 때문에 valid입니다. 그리고 이 정보를 "/"로 구분한 문자열로 나타내면 "male/operation/1team/valid"가 됩니다.

# 일련번호가 저장된 문자열 serial이 주어질 때 일련번호를 해석한 정보를 담은 문자열을 return 하도록 solution 함수를 완성해 보세요.

# 제한사항
# serial의 길이 = 8
# serial에 본문에서 설명한 번호 이외의 번호는 주어지지 않습니다.
# 1 ≤ 소속 팀 번호 N ≤ 99

department_dic = {10: 'operation', 11: 'sales',
                  12: 'develop', 13: 'finance', 14: 'law', 15: 'research'}


def solution(serial):
    data = []
    for i in range(0, len(serial), 2):
        data.append(''.join(list(serial)[i:i+2]))

    sex = 'male' if data[0] == '01' else 'female'
    department = department_dic[int(data[1])]
    team = int(data[2])
    isValid = 'valid' if sum(
        map(int, list(str(serial))[:-2])) % 13 == int(data[3]) else 'invalid'

    return '{}/{}/{}team/{}'.format(sex, department, team, isValid)
