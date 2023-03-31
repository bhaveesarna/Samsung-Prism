#include "sample_files/sample3.h"
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
 TEST(Autotest, switchcase){
EXPECT_EQ(15,  operate(0));
}
 TEST(Autotest, switchcase){
EXPECT_EQ(5,  operate(1));
}
 TEST(Autotest, switchcase){
EXPECT_EQ(50,  operate(2));
}
 TEST(Autotest, switchcase){
EXPECT_EQ(2,  operate(3));
}
 TEST(Autotest, Positive){
EXPECT_EQ(0,  operate(16));
}
 TEST(Autotest, Negative){
EXPECT_EQ(-1,  operate(-63));
}
 TEST(Autotest, Zero){
EXPECT_EQ(15,  operate(0));
}
}