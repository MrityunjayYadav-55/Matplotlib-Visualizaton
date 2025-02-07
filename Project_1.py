import matplotlib.pyplot as plt
import numpy as np

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
organic = [8000, 8500, 8700, 8900, 9100, 9500]
social = [3000, 3200, 3300, 3400, 3600, 3800]
paid = [5000, 5200, 5400, 5500, 5700, 5900]
direct = [4000, 4100, 4200, 4300, 4500, 4700]

traffic_sources = ["Organic", "Social", "Paid", "Direct"]
total_visitors = [sum(organic), sum(social), sum(paid), sum(direct)]

session_durations = [5, 10, 15, 20, 25, 30, 10, 35, 40, 50, 5, 15, 10, 25, 30]
bounce_rates = [[40, 42, 39, 38, 37, 35], 
                [50, 52, 48, 47, 45, 43], 
                [30, 32, 28, 26, 25, 24], 
                [35, 37, 34, 33, 31, 30]]  

fig, ax = plt.subplots(2, 2, figsize = (10, 8))

# for Visitor Comparison :
ax[0, 0].plot(months, organic, marker = 'o', color = 'r', linestyle = '-', label = 'Organic Visitors')
ax[0, 0].plot(months, social, marker = 's', color = 'b', linestyle = '--', label = 'Social Visitors')
ax[0, 0].plot(months, paid, marker = 'D', color = 'g', linestyle = '-.', label = 'Paid Visitors')
ax[0, 0].plot(months, direct, marker = '+', color = 'cyan', linestyle = ':', label = 'Direct Visitors')
ax[0, 0].legend()
ax[0, 0].set_title("Website Monthly Visitors")
ax[0, 0].grid(True)

# for Sources Distribution :
ax[0, 1].bar(traffic_sources, total_visitors, color = ('r', 'orange', 'b', 'purple'))
ax[0, 1].set_title("Traffic Sources Distribution")
ax[0, 1].grid(True)

# for User Engagement Analysis :
ax[1, 0].hist(session_durations, bins = 10, color = 'cyan', edgecolor = 'black')
ax[1, 0].set_title("Engagement Analysis")
ax[1, 0].grid(True)

# for Rate Variability :
ax[1, 1].boxplot(bounce_rates, labels = traffic_sources)
ax[1, 1].set_title("Bounce Rate Variability")
ax[1, 1].grid(True)


plt.tight_layout()
plt.text(0.5, 0.5, "github.com/MrityunjayYadav-55", fontsize = 10, alpha = 0.5)
# plt.savefig("web_traffic_analysis.png", dpi = 300, bbox_inches = 'tight')
plt.show()
