#include "sample2.h"
#include "gtest/gtest.h"
namespace {
class QuickTest : public testing::Test {
protected:
void SetUp() override { start_time_ = time(nullptr); }
void TearDown() override {
	const time_t end_time = time(nullptr);
EXPECT_TRUE(end_time - start_time_ <= 10) << "The test took too long.";
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