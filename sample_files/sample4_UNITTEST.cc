#include "sample_files/sample4.h"
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
EXPECT_TRUE( find_while(9));
}
 TEST(Autotest, loop){
EXPECT_TRUE( find_while(10));
}
 TEST(Autotest, loop){
EXPECT_FALSE( find_while(11));
}
 TEST(Autotest, Positive){
EXPECT_FALSE( find_while(39));
}
 TEST(Autotest, Negative){
EXPECT_FALSE( find_while(-52));
}
 TEST(Autotest, Zero){
EXPECT_TRUE( find_while(0));
}
}