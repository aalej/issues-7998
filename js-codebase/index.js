const {
    onNewNonfatalIssuePublished,
} = require("firebase-functions/v2/alerts/crashlytics");

exports.post_nonfatal_issue_js = onNewNonfatalIssuePublished(async (event) => {
    const appId = event.appId;
    const { id, title, subtitle, appVersion } = event.data.payload.issue;
    const message = `
    🚨 New fatal issue for ${appId} in version ${appVersion} 🚨
    
    **${title}**
    
    ${subtitle}
    
    id: \`${id}\`
    `;
    console.log(message);
});