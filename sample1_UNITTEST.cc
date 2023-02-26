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
EXPECT_EQ(120, factorial(5));
EXPECT_EQ(24, factorial(4));
EXPECT_EQ(6, factorial(3));
EXPECT_EQ(40320, factorial(8));
}
 TEST(IsPrimeTestSuite, PrimeTest1){
EXPECT_EQ(false, IsPrime(10));
EXPECT_EQ(true, IsPrime(3));
}
 TEST(Autotest, Positive){
EXPECT_EQ(1,  Factorial(0));
}
 TEST(Autotest, Negative){
EXPECT_EQ(1,  Factorial(-7));
}
 TEST(Autotest, Content){
EXPECT_FALSE(False,  IsPrime(0));
}
 TEST(Autotest, Content){
EXPECT_FALSE(False,  IsPrime(1));
}
 TEST(Autotest, Content){
EXPECT_TRUE(True,  IsPrime(2));
}
 TEST(Autotest, Positive){
EXPECT_FALSE(False,  IsPrime(4));
}
 TEST(Autotest, Negative){
EXPECT_FALSE(False,  IsPrime(0));
}
}