from src.rules import check_rules


def test(name, message, should_flag):
    flags = check_rules(message)
    ok = (len(flags) > 0) == should_flag
    print("PASS" if ok else "FAIL", "-", name, flags)


test("fee scam", "Pay Rs 2000 registration fee to confirm your job", True)
test("aadhaar scam", "Send your Aadhaar and bank details on WhatsApp for joining", True)
test("typing job scam", "Typing job from home. Earn Rs 5000 per day. No interview", True)
test("real job 1", "We are hiring a Python developer. Apply on our careers page. Two interview rounds.", False)
test("real job 2", "Software engineer role. Skills: Java, SQL. Interview: 1 technical and 1 HR round.", False)