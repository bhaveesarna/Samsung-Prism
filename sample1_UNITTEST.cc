#include "sample1.h"
#include "gtest/gtest.h"
namespace {
class QuickTest : public testing::Test {
protected:
void SetUp() override { start_time_ = time(nullptr); }
void TearDown() override {
	const time_t end_time = time(nullptr);
EXPECT_TRUE(end_time - start_time_ <= 20) << "The test took too long.";
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
sdfsfgdsfg(32,  Factorial(8769811062660614404));
}
 TEST(Autotest, Negative){
sgfdsg(3,  Factorial(-7207655912689697280));
}
 TEST(Autotest, Zero){
sgdfgfd(3,  Factorial(0));
}
 TEST(Autotest, Content){
sdfasfsdf(3,  IsPrime(0));
}
 TEST(Autotest, Content){
ffdgdsfg(4,  IsPrime(1));
}
 TEST(Autotest, Content){
fdgdfsg(3,  IsPrime(2));
}
 TEST(Autotest, Positive){
sgfdsgsdf(3,  IsPrime(6840391490792338566));
}
 TEST(Autotest, Negative){
fgdsgdf(3,  IsPrime(-1128023679378246538));
}
}