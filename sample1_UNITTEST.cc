#include "sample1.h"
#include "gtest/gtest.h"
namespace {
class QuickTest : public testing::Test {
protected:
void SetUp() override { start_time_ = time(nullptr); }
void TearDown() override {
	const time_t end_time = time(nullptr);
EXPECT_TRUE(end_time - start_time_ <= 5) << "The test took too long.";
}
};
 TEST(FactorialTest, Positive){
EXPECT_EQ(120, Factorial(5));
EXPECT_EQ(24, Factorial(4));
EXPECT_EQ(6, Factorial(3));
EXPECT_EQ(40320, Factorial(8));
}
 TEST(IsPrimeTestSuite, PrimeTest1){
EXPECT_EQ(false, IsPrime(10));
EXPECT_EQ(true, IsPrime(3));
}
 TEST(Autotest, Positive){
EXPECT_EQ(362880,  Factorial(9));
}
 TEST(Autotest, Negative){
EXPECT_EQ(1,  Factorial(-7));
}
 TEST(Autotest, Zero){
EXPECT_EQ(1,  Factorial(0));
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
 TEST(Autotest, Positive){
EXPECT_FALSE( IsPrime(9));
}
 TEST(Autotest, Negative){
EXPECT_FALSE( IsPrime(-10));
}
 TEST(Autotest, Zero){
EXPECT_FALSE( IsPrime(0));
}
 TEST(Autotest, Positive){
EXPECT_FALSE( insert(10));
}
 TEST(Autotest, Negative){
EXPECT_FALSE( insert(-8));
}
 TEST(Autotest, Zero){
EXPECT_FALSE( insert(0));
}
}