#include "sample_files/sample2.h"
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
EXPECT_FALSE( find_no(-1));
}
 TEST(Autotest, loop){
EXPECT_TRUE( find_no(0));
}
 TEST(Autotest, loop){
EXPECT_TRUE( find_no(1));
}
 TEST(Autotest, Positive){
EXPECT_FALSE( find_no(92));
}
 TEST(Autotest, Negative){
EXPECT_FALSE( find_no(-100));
}
}