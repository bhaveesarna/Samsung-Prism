#include "sample_files/sample5.h"
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
 TEST(Autotest, MultiArgs){
EXPECT_EQ(0,  add_nums((0, 0)));
}
 TEST(Autotest, MultiArgs){
EXPECT_EQ(-93,  add_nums((0, -93)));
}
 TEST(Autotest, MultiArgs){
EXPECT_EQ(70,  add_nums((0, 70)));
}
 TEST(Autotest, MultiArgs){
EXPECT_EQ(49,  add_nums((49, 0)));
}
 TEST(Autotest, MultiArgs){
EXPECT_EQ(-44,  add_nums((49, -93)));
}
 TEST(Autotest, MultiArgs){
EXPECT_EQ(119,  add_nums((49, 70)));
}
 TEST(Autotest, MultiArgs){
EXPECT_EQ(-91,  add_nums((-91, 0)));
}
 TEST(Autotest, MultiArgs){
EXPECT_EQ(-184,  add_nums((-91, -93)));
}
 TEST(Autotest, MultiArgs){
EXPECT_EQ(-21,  add_nums((-91, 70)));
}
}