#include "sample_files/sample1.h"
#include "gtest/gtest.h"
namespace {
class QuickTest : public testing::Test {
protected:
void SetUp() override { start_time_ = time(nullptr); }
void TearDown() override {
	const time_t end_time = time(nullptr);
EXPECT_TRUE(end_time - start_time_ <= 4) << "The test took too long.";
}
};
 TEST(Autotest, loop){
EXPECT_EQ(1,  Factorial(0));
}
 TEST(Autotest, loop){
EXPECT_EQ(1,  Factorial(1));
}
 TEST(Autotest, loop){
EXPECT_EQ(2,  Factorial(2));
}
 TEST(Autotest, Positive){
EXPECT_EQ(0,  Factorial(35));
}
 TEST(Autotest, Negative){
EXPECT_EQ(1,  Factorial(-68));
}
 TEST(Autotest, BVA){
EXPECT_FALSE( IsPrime(0));
}
 TEST(Autotest, BVA){
EXPECT_FALSE( IsPrime(1));
}
 TEST(Autotest, BVA){
EXPECT_TRUE( IsPrime(2));
}
 TEST(Autotest, BVA){
EXPECT_TRUE( IsPrime(3));
}
 TEST(Autotest, BVA){
EXPECT_FALSE( IsPrime(-1));
}
 TEST(Autotest, loop){
EXPECT_FALSE( IsPrime(4));
}
 TEST(Autotest, Positive){
EXPECT_TRUE( IsPrime(5));
}
 TEST(Autotest, Negative){
EXPECT_FALSE( IsPrime(-22));
}
}